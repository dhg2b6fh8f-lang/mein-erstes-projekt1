"""Kleiner, abhängigkeitsarmer Client für die Jira Cloud REST API v3.

Konfiguration über Umgebungsvariablen (siehe .env.example):
    JIRA_BASE_URL   z. B. https://firma.atlassian.net
    JIRA_EMAIL      E-Mail des (technischen) Nutzers
    JIRA_API_TOKEN  API-Token von id.atlassian.com
"""
from __future__ import annotations

import os
import time
from typing import Any, Iterator

import requests

try:  # .env optional laden
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


def adf_text(text: str) -> dict[str, Any]:
    """Wandelt Klartext (mit Zeilenumbrüchen) in Atlassian Document Format um."""
    paragraphs = []
    for block in text.split("\n\n"):
        content = []
        lines = block.split("\n")
        for i, line in enumerate(lines):
            if line:
                content.append({"type": "text", "text": line})
            if i < len(lines) - 1:
                content.append({"type": "hardBreak"})
        paragraphs.append({"type": "paragraph", "content": content})
    return {"type": "doc", "version": 1, "content": paragraphs}


class JiraClient:
    def __init__(self, base_url: str | None = None, email: str | None = None, token: str | None = None):
        self.base_url = (base_url or os.environ["JIRA_BASE_URL"]).rstrip("/")
        self.session = requests.Session()
        self.session.auth = (email or os.environ["JIRA_EMAIL"], token or os.environ["JIRA_API_TOKEN"])
        self.session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})

    # ---------- Basis ----------
    def request(self, method: str, path: str, **kwargs: Any) -> Any:
        url = f"{self.base_url}/rest/api/3/{path.lstrip('/')}"
        for attempt in range(5):
            resp = self.session.request(method, url, timeout=30, **kwargs)
            if resp.status_code == 429:  # Rate Limit: warten und wiederholen
                wait = int(resp.headers.get("Retry-After", 2 ** attempt))
                time.sleep(wait)
                continue
            if not resp.ok:
                raise RuntimeError(f"{method} {path} -> {resp.status_code}: {resp.text[:500]}")
            return resp.json() if resp.content else None
        raise RuntimeError(f"{method} {path}: Rate Limit nach mehreren Versuchen")

    def get(self, path: str, **params: Any) -> Any:
        return self.request("GET", path, params=params)

    def post(self, path: str, body: dict[str, Any]) -> Any:
        return self.request("POST", path, json=body)

    def put(self, path: str, body: dict[str, Any]) -> Any:
        return self.request("PUT", path, json=body)

    # ---------- Suche ----------
    def search(self, jql: str, fields: list[str] | None = None, page_size: int = 100) -> Iterator[dict[str, Any]]:
        """Alle Vorgänge zu einer JQL-Abfrage (neuer Endpunkt /search/jql mit nextPageToken)."""
        token = None
        while True:
            body: dict[str, Any] = {"jql": jql, "maxResults": page_size, "fields": fields or ["*navigable"]}
            if token:
                body["nextPageToken"] = token
            data = self.post("search/jql", body)
            yield from data.get("issues", [])
            token = data.get("nextPageToken")
            if not token or data.get("isLast", False):
                break

    # ---------- Vorgänge ----------
    def get_issue(self, key: str) -> dict[str, Any]:
        return self.get(f"issue/{key}")

    def create_issue(
        self,
        project_key: str,
        summary: str,
        issue_type: str = "Task",
        description: str | None = None,
        extra_fields: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        fields: dict[str, Any] = {
            "project": {"key": project_key},
            "summary": summary,
            "issuetype": {"name": issue_type},
        }
        if description:
            fields["description"] = adf_text(description)
        if extra_fields:
            fields.update(extra_fields)
        return self.post("issue", {"fields": fields})

    def add_comment(self, key: str, text: str) -> dict[str, Any]:
        return self.post(f"issue/{key}/comment", {"body": adf_text(text)})

    def transition(self, key: str, target_status: str) -> None:
        """Übergang über den Namen des Zielstatus ausführen."""
        transitions = self.get(f"issue/{key}/transitions")["transitions"]
        for t in transitions:
            if t["to"]["name"].lower() == target_status.lower() or t["name"].lower() == target_status.lower():
                self.post(f"issue/{key}/transitions", {"transition": {"id": t["id"]}})
                return
        names = [t["to"]["name"] for t in transitions]
        raise ValueError(f"Kein Übergang nach '{target_status}' möglich. Möglich: {names}")

    # ---------- Hilfen ----------
    def find_account_id(self, email_or_name: str) -> str | None:
        users = self.get("user/search", query=email_or_name)
        return users[0]["accountId"] if users else None

    def fields(self) -> list[dict[str, Any]]:
        return self.get("field")


if __name__ == "__main__":
    jira = JiraClient()
    me = jira.get("myself")
    print(f"Verbunden als {me['displayName']} ({me['accountId']})")
