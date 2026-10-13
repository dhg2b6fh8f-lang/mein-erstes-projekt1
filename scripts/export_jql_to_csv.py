"""Exportiert das Ergebnis einer JQL-Abfrage als CSV (für Excel/Power BI).

Aufruf:
    python export_jql_to_csv.py "project = SVC AND created >= -30d" export.csv
"""
import csv
import sys

from jira_client import JiraClient

FIELDS = ["summary", "status", "issuetype", "priority", "assignee", "reporter", "created", "resolutiondate", "duedate"]


def name(value):
    """Holt den lesbaren Namen aus verschachtelten Jira-Objekten."""
    if isinstance(value, dict):
        return value.get("displayName") or value.get("name") or value.get("value") or ""
    return value or ""


def main() -> None:
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    jql, out = sys.argv[1], sys.argv[2]
    jira = JiraClient()

    count = 0
    with open(out, "w", newline="", encoding="utf-8-sig") as fh:
        writer = csv.writer(fh, delimiter=";")
        writer.writerow(["key"] + FIELDS)
        for issue in jira.search(jql, fields=FIELDS):
            f = issue["fields"]
            writer.writerow([issue["key"]] + [name(f.get(field)) for field in FIELDS])
            count += 1
    print(f"{count} Vorgänge nach {out} exportiert")


if __name__ == "__main__":
    main()
