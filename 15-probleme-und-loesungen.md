# 15 – Probleme & Lösungen (Wissensdatenbank)

Typische Probleme aus Atlassian Community, Knowledge-Base-Artikeln und Praxisberichten – jeweils mit Ursache und Lösung. Zum schnellen Nachschlagen bei Kunden.

**Erste Regel bei jedem Problem:** Erst Ursache finden, dann ändern. Und prüfen, ob das betroffene Scheme von anderen Projekten mitgenutzt wird.

---

## A. Felder

### Feld wird nicht angezeigt oder ist nicht bearbeitbar
**Erst prüfen:** Company-managed oder team-managed? (unten links in der Projekt-Seitenleiste)

**Company-managed – Ursachen nacheinander prüfen:**
1. **Feld fehlt auf dem Screen** oder liegt auf einem anderen Reiter → Projekteinstellungen → Screens → Screen für Vorgangstyp und Aktion (Erstellen/Bearbeiten/Anzeigen) öffnen, alle Reiter prüfen, Feld hinzufügen. *Achtung: Screens können geteilt sein.*
2. **Feld im Layout versteckt** („Ausblenden, wenn leer“ oder „Ausgeblendet“) → Layout des Vorgangstyps bearbeiten, Feld in sichtbaren Bereich ziehen.
3. **Feld in der Feldkonfiguration ausgeblendet** → Projekteinstellungen → Felder → Feld „Anzeigen“.
4. **Feldkontext schließt Projekt oder Vorgangstyp aus** → Einstellungen → Vorgänge → Benutzerdefinierte Felder → Kontexte → Projekt/Vorgangstyp hinzufügen.
5. **Fehlende Rechte** (Vorgänge bearbeiten) oder **Workflow-Eigenschaft** sperrt Bearbeitung im aktuellen Status.

**Team-managed:** Projekteinstellungen → Vorgangstypen → Feld aus „Ausgeblendete Felder“ nach oben ziehen oder neu anlegen. Hier gibt es nur eine Maske für Erstellen, Anzeigen und Bearbeiten.

**Werkzeug:** Atlassian bietet eine Funktion „Fehlende Felder finden“ in der Administration – zeigt, warum ein Feld fehlt.

### Zu viele Felder, alles unübersichtlich
**Ursache:** Felder ohne Konzept angelegt, nie gelöscht.
**Lösung (bewährt):**
1. Alle Felder in einer Liste erfassen: Name, Typ, Screens, Kontexte, letzte Verwendung
2. Fachbereiche markieren „behalten“ oder „löschen“
3. Ähnliche Felder zusammenführen und allgemeiner machen
4. Kontexte auf die nötigen Projekte begrenzen
5. Regel einführen: neues Feld nur mit Begründung beim Jira-Owner

---

## B. Berechtigungen

### Nutzer sieht ein Projekt oder einen Vorgang nicht
1. **Recht „Projekte durchsuchen“** fehlt (häufigster Fall!)
2. Nutzer ist nicht in der richtigen **Projektrolle/Gruppe**
3. **Sicherheitsstufe** am Vorgang
4. Nutzer hat **keine Produktlizenz** (z. B. Zugriff auf JSM, aber nicht auf Jira)

**Werkzeug:** **Berechtigungshilfe** (Permission Helper) in den Projekteinstellungen – zeigt, ob und warum ein Nutzer etwas darf.

### Die 13 häufigsten Berechtigungsfehler
1. Rechte an einzelne Personen statt an Gruppen/Rollen vergeben
2. Breiten Zugriff „für alle Fälle“ geben
3. Nur Gruppen nutzen, Projektrollen ignorieren → doppelte Schemes
4. Rechte einmal setzen und nie wieder prüfen
5. So restriktiv sein, dass für alles der Admin nötig ist
6. Ähnliche Projekte ohne Grund unterschiedlich einrichten
7. Annehmen, dass alle das Rechtekonzept verstehen
8. Globale Rechte nutzen, wo Projektrechte reichen
9. Für jedes Projekt ein neues Berechtigungsschema
10. „Projekte durchsuchen“ vergessen
11. Gruppen und Rollen ohne klare Logik mischen
12. Berechtigungshilfe nicht nutzen
13. Abweichungen vom Standard nicht dokumentieren

**Bewährte Logik:** Gruppen für breiten, zentral verwalteten Zugang · Projektrollen für Verantwortungen im Projekt · Einzelpersonen nur für kurzfristige Ausnahmen.

---

## C. Automation

### Regel startet nicht
| Ursache | Lösung |
|---|---|
| Regel deaktiviert | Aktivieren |
| Auslöser kommt von einer anderen Regel | In den Regeldetails „Andere Regeln dürfen diese Regel auslösen“ aktivieren |
| Vorgänge kamen über den **CSV-Import „Externe Systeme“** | Dieser Import löst „Vorgang erstellt“ nicht aus → anderen Import nutzen oder geplante Regel |
| Erstellen-Übergang im Workflow feuert falsches Ereignis | Erstellen-Übergang muss das Ereignis „Vorgang erstellt“ auslösen |
| Ereignis im Workflow passt nicht zum Auslöser der Regel | Ereignis und Auslöser angleichen |
| Geltungsbereich der Regel umfasst das Projekt nicht | Geltungsbereich erweitern |
| Ausführender (Actor) hat keine Rechte | Rechte prüfen oder Actor ändern |
| Limit erreicht | Verbrauch prüfen (siehe Kapitel 16) |

**Immer zuerst:** Audit-Log der Regel ansehen.

### Regeln lösen sich gegenseitig aus (Schleife)
**Lösung:** „Andere Regeln dürfen auslösen“ nur gezielt aktivieren, Bedingungen ergänzen, Ketten in eine Regel zusammenlegen.

### Automation wird teuer (ab 03.12.2026 Abrechnung nach Schritten)
Siehe [Kapitel 16](16-aktuelle-updates.md#3-automation-wird-nach-schritten-abgerechnet).

---

## D. Jira Service Management

### Antworten per E-Mail erzeugen neue Tickets statt Kommentare
| Ursache | Lösung |
|---|---|
| Vorgangsschlüssel fehlt in Betreff/Text | `[KEY-123]` im Betreff erhalten, Kunden bitten, auf die Benachrichtigung zu antworten |
| Absender hat keinen Zugriff auf das Ticket | Als Anfrageteilnehmer hinzufügen oder mit der Organisation teilen |
| Antwort von anderer Mailadresse | Adresse zum Konto hinzufügen bzw. Teilnehmer ergänzen |
| Doppelte Kundenkonten (Portal-Konto + Atlassian-Konto mit gleicher Mail) | In der Administration Portal-Konto mit Atlassian-Konto zusammenführen |
| Workflow-Eigenschaft verbietet Kommentare im aktuellen Status (oft im End-Status) | Eigenschaft im Workflow-Editor prüfen |
| Externe Mails mit gültigem Schlüssel werden nicht angenommen | E-Mail-Einstellung aktivieren, die solche Mails als Kommentar akzeptiert |

**Werkzeug:** **E-Mail-Protokoll** in den Space-Einstellungen zeigt, welche Mail was ausgelöst hat.
**Sonderfall Microsoft 365:** Sicherheitsfunktionen wie „Dynamic Delivery“ können Mails mehrfach zustellen → mit der IT des Kunden klären.

### SLA läuft falsch
- Kein **Kalender** hinterlegt → läuft nachts und am Wochenende
- Pause-Bedingung fehlt für „Warten auf Kunde“
- SLA-Ziele nach Priorität nicht in der richtigen Reihenfolge (Jira nimmt das **erste** passende Ziel)

### Kunden finden ihre Tickets nicht
- Im Portal „Anfragen“ zeigen, Filter „Erstellt von mir / Meine Organisation“
- Organisationen nutzen, damit Kollegen Tickets des eigenen Unternehmens sehen

### Unerwartete Lizenzkosten
- Prüfen, ob Kunden versehentlich als **Agents** (zahlend) statt als Portal-Kunden angelegt werden
- Nutzer-Bereitstellung (Gruppen mit Produktzugriff) kontrollieren

---

## E. Benachrichtigungen

### „Wir bekommen zu viele Mails“
1. **Benachrichtigungsschema** ausdünnen: nur Bearbeiter, Melder, Beobachter (vorher prüfen, ob geteilt)
2. **Automationen und Apps** prüfen, die zusätzlich Mails versenden – oft doppelte Regeln
3. Jira Cloud fasst Änderungen innerhalb kurzer Zeit zu einer Mail zusammen – Nutzer auf ihre **persönlichen Einstellungen** hinweisen
4. Für Teams: Benachrichtigungen lieber in **Teams/Slack-Kanäle** statt Einzelmails

---

## F. Performance

### Jira Cloud ist langsam
| Ursache | Lösung |
|---|---|
| Sehr große Datenmengen an einer Stelle (z. B. 1.000 Vorgänge unter einem Epic, 5.000 Kommentare) | Aufteilen |
| Regeln, die alle offenen Vorgänge anfassen | Umfang begrenzen |
| Großer Suchindex | Alte Projekte archivieren |
| Automations-Ketten | Vereinfachen |
| Integrationen mit Tausenden API-Aufrufen | Aufrufe bündeln, Intervall verlängern |
| App-Konflikte | Apps einzeln deaktivieren, um den Verursacher zu finden |
| Viele benutzerdefinierte Felder | Kontexte einschränken, Felder bereinigen |

---

## G. Technische Schulden aufräumen (Health Check)

**Ursachen:** zu kreative Lösungen, keine Pflege, alte Daten, verteilte Admins ohne Absprache, Admin-Wechsel ohne Doku.

**Ablauf:**
1. **Alte Projekte archivieren** (umkehrbar – im Zweifel archivieren)
2. **Alte Vorgänge löschen** (nicht umkehrbar!) – vorher als CSV exportieren. Kandidaten: erledigt, älter als 3 Jahre, seit 1 Jahr nicht angesehen
3. **Felder bereinigen** (siehe A)
4. **Boards, Workflows, Status, Screens, Vorgangstypen, Rollen** aufräumen
5. **Rückfall verhindern:** wenige Admins, Projektvorlagen, Felder wiederverwenden, klare Namen, regelmäßige Aufräumtermine

→ Daraus lässt sich ein **festes Beratungspaket** machen: „Jira Health Check & Aufräumen“.

---

## H. KI / Rovo-Agents liefern schlechte Ergebnisse

**Ursache meistens:** schlechte Datenqualität, nicht der Agent.
- Leere Komponenten → Agent kann nicht zuordnen
- Alles hat Priorität „Mittel“ → nichts kann eskaliert werden
- Vage Beschreibungen → keine Verknüpfung zu Wissen

**Lösung:**
1. Erst klären, **welche Entscheidungen** der Agent treffen soll → diese Felder zur Pflicht machen
2. Agent-Anweisungen **schrittweise und konkret** formulieren
3. **Umfang begrenzen**: nur nötige Wissensquellen und Rechte, Auslöser per JQL filtern
4. **Ein Agent = eine Aufgabe**, mehrere Agents über Automation verketten
5. Agent soll **jeden bearbeiteten Vorgang kommentieren** (Nachvollziehbarkeit)
6. Mit **einem** Prozess mit viel Volumen starten (Helpdesk, Bugs)
7. **Kosten:** Rovo-Credits pro Nutzer begrenzt – Pilot mit festem Budget (siehe Kapitel 16)

---

## I. Neue Oberfläche verwirrt Nutzer

### „Wo ist die Zusammenfassung beim Erstellen?“ / Erstellen-Maske verändert
Admins können in den allgemeinen Einstellungen eine **einfache Erstellen-Maske** („Simple create“) aktivieren.

### „Wo sind die Sprint-Reports?“
Der alte Reiter „Berichte“ wurde zu **Space-Dashboards**. Sprint-Reports sind weiter vorhanden, aber an anderer Stelle – Schulungsunterlagen anpassen.

### „Projekte heißen jetzt Spaces?“
Ja – siehe [Kapitel 16](16-aktuelle-updates.md). JQL `project = ABC` funktioniert vorerst weiter.
