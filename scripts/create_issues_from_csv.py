"""Legt Vorgänge aus einer CSV-Datei an (z. B. Export aus Excel, Trennzeichen ';').

Erwartete Spalten (Kopfzeile):
    summary;description;issuetype;priority;assignee_email;duedate;labels
    - duedate im Format JJJJ-MM-TT
    - labels durch Komma getrennt

Aufruf:
    python create_issues_from_csv.py beispiel.csv PROJ            # Testlauf, legt nichts an
    python create_issues_from_csv.py beispiel.csv PROJ --ausfuehren
"""
import csv
import sys

from jira_client import JiraClient


def main() -> None:
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    path, project = sys.argv[1], sys.argv[2]
    dry_run = "--ausfuehren" not in sys.argv
    jira = JiraClient()
    account_cache: dict[str, str | None] = {}

    with open(path, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh, delimiter=";"))

    print(f"{len(rows)} Zeilen gelesen. {'TESTLAUF – nichts wird angelegt.' if dry_run else 'Lege Vorgänge an …'}")

    for n, row in enumerate(rows, start=2):  # Zeile 1 = Kopfzeile
        summary = (row.get("summary") or "").strip()
        if not summary:
            print(f"Zeile {n}: übersprungen (keine Zusammenfassung)")
            continue

        extra: dict = {}
        if row.get("priority"):
            extra["priority"] = {"name": row["priority"].strip()}
        if row.get("duedate"):
            extra["duedate"] = row["duedate"].strip()
        if row.get("labels"):
            extra["labels"] = [l.strip().replace(" ", "-") for l in row["labels"].split(",") if l.strip()]
        email = (row.get("assignee_email") or "").strip()
        if email:
            if email not in account_cache:
                account_cache[email] = jira.find_account_id(email)
            if account_cache[email]:
                extra["assignee"] = {"accountId": account_cache[email]}
            else:
                print(f"Zeile {n}: Bearbeiter {email} nicht gefunden – bleibt leer")

        issue_type = (row.get("issuetype") or "Task").strip()
        if dry_run:
            print(f"Zeile {n}: würde anlegen [{issue_type}] {summary} {extra}")
            continue
        try:
            created = jira.create_issue(project, summary, issue_type, row.get("description"), extra)
            print(f"Zeile {n}: {created['key']} angelegt")
        except RuntimeError as err:
            print(f"Zeile {n}: FEHLER {err}")


if __name__ == "__main__":
    main()
