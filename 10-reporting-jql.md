# 10 – Reporting & JQL

## JQL-Grundlagen

```
Feld  Operator  Wert   [AND|OR]  ...   ORDER BY Feld ASC|DESC
```

| Operator | Bedeutung | Beispiel |
|---|---|---|
| `=` / `!=` | gleich / ungleich | `status = "In Bearbeitung"` |
| `IN` / `NOT IN` | in Liste | `priority IN (Hoch, Kritisch)` |
| `~` | enthält Text | `summary ~ "Pumpe"` |
| `IS EMPTY` / `IS NOT EMPTY` | leer / gefüllt | `assignee IS EMPTY` |
| `>` `<` `>=` `<=` | Vergleich | `created >= -7d` |
| `WAS` | war früher mal | `status WAS "Gelöst"` |
| `CHANGED` | wurde geändert | `status CHANGED TO "Erledigt" DURING (startOfMonth(), now())` |

## Nützliche Funktionen
`currentUser()`, `now()`, `startOfDay()`, `startOfWeek()`, `startOfMonth()`, `endOfMonth()`, `membersOf("gruppe")`, `openSprints()`, `unreleasedVersions()`

## JQL-Spickzettel (Kopiervorlagen)

| Zweck | JQL |
|---|---|
| Meine offenen Vorgänge | `assignee = currentUser() AND statusCategory != Done ORDER BY priority DESC` |
| Nicht zugewiesen | `project = SVC AND assignee IS EMPTY AND statusCategory != Done` |
| Überfällig | `duedate < now() AND statusCategory != Done` |
| Diese Woche erstellt | `created >= startOfWeek()` |
| Letzten Monat erledigt | `resolved >= startOfMonth(-1) AND resolved < startOfMonth()` |
| Lange liegengeblieben | `statusCategory != Done AND updated <= -14d` |
| Kritisch & offen | `priority = Kritisch AND statusCategory != Done` |
| Wieder geöffnet | `status CHANGED FROM "Gelöst" TO "In Bearbeitung"` |
| Team-Auslastung | `assignee IN membersOf("jira-service-agents") AND statusCategory = "In Progress"` |
| Ohne Epic | `issuetype in (Story, Task) AND parent IS EMPTY AND statusCategory != Done` |
| JSM: SLA verletzt | `"Time to resolution" = breached()` |
| JSM: SLA läuft bald ab | `"Time to resolution" < remaining("4h")` |
| JSM: Wartet auf Kunde | `status = "Warten auf Kunde"` |

## Dashboards – Vorschlag je Zielgruppe

**Team-Dashboard**
- Gefilterte Liste „Meine offenen Vorgänge“
- Zweidimensionale Statistik: Bearbeiter × Status
- Erstellt vs. erledigt (30 Tage)

**Leitungs-Dashboard**
- Kreisdiagramm: offene Vorgänge nach Priorität / Komponente
- Durchschnittsalter offener Vorgänge
- Erstellt vs. erledigt (90 Tage)
- JSM: SLA-Erfolgsquote

**Projekt-/Auftrags-Dashboard (Maschinenbau)**
- Liste aller Auftrags-Epics mit Fortschritt
- Überfällige Arbeitspakete
- Zeitachse/Roadmap

## Kennzahlen, die Kunden wirklich nutzen

| Kennzahl | Bedeutung | Wie messen |
|---|---|---|
| Durchlaufzeit | Wie lange dauert ein Vorgang von Start bis Ende? | Kontrolldiagramm (Kanban-Board) |
| Erstellt vs. erledigt | Wächst der Rückstau? | Gadget „Erstellt vs. erledigt“ |
| SLA-Einhaltung | Werden Zusagen eingehalten? | JSM-Reports |
| Erstlösungsquote | Wie viele Anfragen ohne Rückfrage gelöst? | JQL mit `status WAS NOT "Warten auf Kunde"` |
| Wiederöffnungsquote | Qualität der Lösungen | JQL „Wieder geöffnet“ |
| Kundenzufriedenheit | JSM-Umfrage nach Lösung | JSM-Report Zufriedenheit |

> **Betriebsrat-Hinweis:** Auswertungen auf Personenebene (wer hat wie viel erledigt) können mitbestimmungspflichtig sein. Team-Kennzahlen sind meist unkritischer.

## Weiter gehen
- **Export:** Filterergebnis als CSV → Excel/Power BI
- **Power BI / Tableau:** Über REST API oder Marketplace-Connectoren
- **Skript:** [scripts/export_jql_to_csv.py](scripts/export_jql_to_csv.py)
