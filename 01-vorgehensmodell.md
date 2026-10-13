# 01 – Vorgehensmodell

Jede Einführung folgt acht Phasen. Kleine Projekte (1 Team, < 20 Nutzer) schaffen das in 2–4 Wochen, größere (mehrere Abteilungen, JSM, Integrationen) in 2–4 Monaten.

```
Vorgespräch → Discovery → Konzept → Aufbau (Sandbox) → Pilot → Rollout → Hypercare → Betrieb
```

---

## Phase 0 – Vorgespräch (30–60 Min.)
**Ziel:** Passt der Kunde? Was ist das eigentliche Problem?
- Schmerzpunkte verstehen („Wir verlieren Aufträge in E-Mails“, „Niemand weiß, wer was macht“)
- Grobe Größe: Nutzer, Abteilungen, bestehende Tools
- Budget- und Zeitrahmen
- **Ergebnis:** Grobangebot (siehe [Angebot-Pakete](vorlagen/angebot-pakete.md))

## Phase 1 – Discovery (1–3 Workshops)
**Ziel:** Ist-Prozesse vollständig verstehen.
- Prozesse mit den Leuten aufnehmen, die sie täglich machen – nicht nur mit dem Chef
- Prozess als Ablauf zeichnen (Start → Schritte → Entscheidungen → Ende)
- Rollen, Übergaben, Engpässe, Pflichtinformationen je Schritt
- Bestehende Daten (Excel-Listen, alte Tickets) einsammeln
- **Ergebnis:** ausgefüllte [Discovery-Checkliste](02-discovery-checkliste.md), Prozessbilder

## Phase 2 – Konzept
**Ziel:** Bauplan, den der Kunde unterschreibt.
- Projektstruktur, Vorgangstypen, Hierarchie
- Workflows je Vorgangstyp
- Felder (Pflicht/optional), Screens
- Berechtigungen und Rollen
- Automationen, Integrationen, Reports
- Migrationsumfang
- **Ergebnis:** [Konzept-Dokument](vorlagen/konzept.md), vom Kunden freigegeben

> **Regel:** Ohne freigegebenes Konzept wird nicht gebaut. Änderungen danach = Change Request (Aufwand neu schätzen).

## Phase 3 – Aufbau
**Ziel:** Konfiguration in einer Testumgebung.
- Premium-Plan: **Sandbox** nutzen. Free/Standard: eigenes Testprojekt oder Test-Site
- Reihenfolge: Felder → Vorgangstypen → Workflows → Screens → Schemes → Projekt → Berechtigungen → Automation → Dashboards
- Alles dokumentieren (was, warum, wo) – später Basis fürs [Betriebshandbuch](vorlagen/betriebshandbuch.md)
- Interner Test mit echten Beispielfällen
- **Ergebnis:** funktionierende Konfiguration + Testprotokoll

## Phase 4 – Pilot (1–2 Wochen)
**Ziel:** Ein kleines Team arbeitet echt damit.
- 3–8 motivierte Nutzer, ein klar abgegrenzter Prozess
- Tägliches kurzes Feedback, wöchentlich nachschärfen
- **Ergebnis:** Feedbackliste, angepasste Konfiguration, Go/No-Go-Entscheidung

## Phase 5 – Rollout
**Ziel:** Alle Nutzer arbeiten im neuen System.
- Migration der Altdaten (siehe [Migration](08-migration.md))
- Schulungen je Rolle (siehe [Rollout & Schulung](11-rollout-schulung.md))
- Altes System auf „nur lesen“ stellen
- [Go-Live-Checkliste](vorlagen/go-live-checkliste.md) abhaken
- **Ergebnis:** [Abnahmeprotokoll](vorlagen/abnahmeprotokoll.md)

## Phase 6 – Hypercare (2–4 Wochen)
**Ziel:** Schnelle Hilfe, damit niemand zurück zu Excel flüchtet.
- Feste Sprechstunde, kurzer Draht für Fragen
- Kleine Anpassungen sofort, größere sammeln
- Nutzung messen (Wer erstellt/bearbeitet Vorgänge?)

## Phase 7 – Betrieb
**Ziel:** Laufende Einnahmen und zufriedener Kunde.
- Wartungsvertrag (z. B. X Stunden/Monat): Anpassungen, neue Automationen, Nutzerverwaltung
- Quartals-Review: Was läuft gut, was fehlt?
- Atlassian-Änderungen beobachten (neue Features, Preisänderungen)

---

## Rollen im Projekt (RACI)

| Aufgabe | Berater (du) | Kunde: Projektleitung | Kunde: Fachbereich | Kunde: IT |
|---|---|---|---|---|
| Discovery | R | A | C | C |
| Konzept | R | A | C | C |
| Aufbau | R/A | I | I | C |
| Test & Pilot | R | A | R | I |
| Migration | R | A | C | C |
| Schulung | R | A | I | I |
| Betrieb | C | A | I | R |

R = macht es, A = entscheidet/verantwortet, C = wird gefragt, I = wird informiert

---

## Typische Fehler – und wie du sie vermeidest

| Fehler | Gegenmittel |
|---|---|
| Altes Chaos 1:1 in Jira nachbauen | Prozess erst vereinfachen, dann abbilden |
| Zu viele Status und Pflichtfelder | Max. 5–7 Status pro Workflow, nur wirklich nötige Pflichtfelder |
| Jedes Team eigene Felder/Workflows | Gemeinsame Schemes, Felder wiederverwenden |
| Keine klaren Admin-Zuständigkeiten | Ein benannter Jira-Owner beim Kunden |
| Schulung nur einmal | Kurze Rollen-Schulungen + Spickzettel + Champions |
| Kein Konzept, direkt bauen | Konzept-Freigabe als Pflicht |
