# 08 – Migration

## Arten von Migrationen

| Von | Nach | Werkzeug |
|---|---|---|
| Excel / CSV | Jira Cloud | Eingebauter CSV-Import (Einstellungen → System → Externe Systemimporte) oder [Skript](scripts/create_issues_from_csv.py) |
| Trello, Asana, Monday | Jira Cloud | Eingebaute Importer bzw. CSV-Export → CSV-Import |
| Anderes Ticketsystem (OTRS, Zendesk…) | JSM | CSV/JSON-Export + Import, ggf. Marketplace-Migrations-App |
| Jira Data Center / Server | Jira Cloud | **Jira Cloud Migration Assistant (JCMA)** – kostenlos von Atlassian |
| Jira Cloud | Jira Cloud (Site-Zusammenlegung) | Cloud-zu-Cloud-Migration (Atlassian) |

## Data Center → Cloud (wichtigstes Geschäftsfeld bis 2029)

Data-Center-Abos laufen am **28.03.2029** aus. Ablauf:

1. **Bestandsaufnahme:** Projekte, Nutzer, Apps, Custom Fields, Workflows, Datenmenge, Anhänge
2. **Aufräumen:** Ungenutzte Projekte archivieren, doppelte Felder zusammenlegen, alte Workflows löschen
3. **Apps prüfen:** Gibt es jede App in der Cloud? Datenmigration der App möglich? Alternativen?
4. **Nutzer & Gruppen:** Mit Atlassian Guard / Entra ID abgleichen
5. **Testmigration** in eine Test-Cloud-Site (immer!)
6. **Abnahme durch Fachbereiche** auf Test-Site
7. **Produktivmigration** (meist am Wochenende), vorher Freeze
8. **Nacharbeiten:** Automationen neu bauen (Script-Runner-Skripte laufen in der Cloud anders!), Links prüfen
9. **Hypercare**

## CSV-Import (Excel → Jira) – Vorgehen

1. Spalten vorbereiten: Zusammenfassung, Beschreibung, Vorgangstyp, Status, Priorität, Bearbeiter (E-Mail), Melder, Fälligkeitsdatum, Komponente, Labels, benutzerdefinierte Felder
2. **Datumsformat** einheitlich (z. B. `dd.MM.yyyy`) – beim Import angeben
3. **Hierarchie:** Spalte „Issue Id“ + „Parent Id“ für Unteraufgaben/Epics
4. Mehrere Werte (Labels, Komponenten): mehrere Spalten mit gleichem Namen
5. Erst **10 Testzeilen** importieren, prüfen, dann alles
6. Mapping-Konfiguration speichern (wiederverwendbar)

## Daten-Hygiene vor jeder Migration
- [ ] Dubletten entfernen
- [ ] Ehemalige Mitarbeiter → auf Platzhalter oder Teamleitung mappen
- [ ] Freitext-Werte vereinheitlichen („Fa. Müller“, „Müller GmbH“ → eins)
- [ ] Alte, erledigte Daten: wirklich nötig? Oft reicht Export als Archiv
- [ ] Anhänge: Größe prüfen (Free-Plan nur 2 GB)

## Migrations-Risiken

| Risiko | Gegenmaßnahme |
|---|---|
| Daten falsch zugeordnet | Testmigration + Stichproben-Prüfung durch Fachbereich |
| Apps fehlen in Cloud | Frühzeitig Alternativen klären |
| Lange Ausfallzeit | Delta-Migration, Wochenende, klarer Freeze |
| Nutzer finden sich nicht zurecht | Schulung vor Go-Live, Spickzettel |
| Automationen/Skripte brechen | Liste aller Automationen, in Cloud neu bauen und testen |
