# Skripte für die Jira Cloud API

Kleine Python-Werkzeuge für typische Aufgaben in Einführungsprojekten.

| Skript | Wofür |
|---|---|
| [jira_client.py](jira_client.py) | Wiederverwendbarer Client: Suche, Vorgänge anlegen/ändern, Kommentare, Übergänge, Rate-Limit-Handling |
| [list_fields.py](list_fields.py) | Feld-IDs nachschlagen (für Smart Values & API) |
| [create_issues_from_csv.py](create_issues_from_csv.py) | Vorgänge aus Excel/CSV anlegen (mit Testlauf) |
| [export_jql_to_csv.py](export_jql_to_csv.py) | JQL-Ergebnis als CSV exportieren |
| [webhook_receiver.py](webhook_receiver.py) | Webhooks/Automation-Webanfragen empfangen |
| [beispiel.csv](beispiel.csv) | Beispieldatei für den CSV-Import |

## Einrichtung

```bash
cd scripts
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env               # dann .env ausfüllen
python jira_client.py              # Verbindungstest
```

**API-Token erstellen:** id.atlassian.com → Sicherheit → API-Token erstellen. Für Kundenprojekte einen **technischen Nutzer** mit nur den nötigen Rechten verwenden.

## Beispiele

```bash
# Feld-ID für "Seriennummer" finden
python list_fields.py serien

# CSV-Import erst testen, dann ausführen
python create_issues_from_csv.py beispiel.csv TEST
python create_issues_from_csv.py beispiel.csv TEST --ausfuehren

# Alle offenen Vorgänge exportieren
python export_jql_to_csv.py "project = TEST AND statusCategory != Done" offen.csv
```

## Eigene Skripte schreiben

```python
from jira_client import JiraClient

jira = JiraClient()
for issue in jira.search("project = SVC AND priority = Kritisch AND statusCategory != Done", ["summary"]):
    jira.add_comment(issue["key"], "Bitte heute priorisieren.")
```

## Sicherheit
- `.env` und Tokens **nie** ins Repo laden (`.gitignore` ist vorbereitet)
- Erst immer an einem **Testprojekt** ausprobieren
- Bei Kundensystemen: schriftliche Freigabe für Skript-Einsatz
