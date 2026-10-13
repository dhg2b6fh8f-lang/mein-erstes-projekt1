"""Listet alle Felder mit ID – nötig für Automation-Smart-Values und API-Aufrufe.

Aufruf:  python list_fields.py            (alle Felder)
         python list_fields.py serien     (nur Felder, deren Name 'serien' enthält)
"""
import sys

from jira_client import JiraClient

jira = JiraClient()
needle = sys.argv[1].lower() if len(sys.argv) > 1 else ""

for f in sorted(jira.fields(), key=lambda f: f["name"].lower()):
    if needle in f["name"].lower():
        kind = "benutzerdefiniert" if f.get("custom") else "Standard"
        ftype = f.get("schema", {}).get("type", "-")
        print(f"{f['id']:<22} {f['name']:<40} {kind:<18} {ftype}")
