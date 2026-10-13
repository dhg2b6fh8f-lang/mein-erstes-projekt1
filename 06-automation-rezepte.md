# 06 – Automation-Rezepte

Jira Automation (eingebaut in Cloud) arbeitet nach dem Muster **Auslöser → Bedingung(en) → Aktion(en)**.

> Atlassian hat 2025 „Issue“ in „Work item“ umbenannt. Je nach Sprache/Version heißen Auslöser z. B. „Vorgang erstellt“, „Arbeitselement erstellt“ oder „Work item created“. Die Logik bleibt gleich.

## Best Practices
- **Geltungsbereich:** Regel nur auf die nötigen Projekte begrenzen (spart Ausführungen und Fehler)
- **Ausführender (Actor):** Standard „Automation for Jira“ – bei Berechtigungsproblemen prüfen
- **Limits:** Free 150 Schritte pro Abo, Standard 400 / Premium 750 / Enterprise 1.000 pro Nutzer und Monat. Geplante Regeln mit großen JQL-Abfragen kosten viel – sparsam takten
- **Audit-Log** jeder Regel nach dem Anlegen prüfen
- **Schleifen vermeiden:** Option „Andere Regeln dürfen diese Regel auslösen“ nur gezielt aktivieren
- **Benennung:** `[PROJ] Auslöser → Ergebnis`
- **Erst im Testprojekt bauen**, dann kopieren

---

## Rezepte

### 1. Automatisch zuweisen nach Komponente
- **Auslöser:** Vorgang erstellt
- **Bedingung:** Komponente ist „Elektrik“
- **Aktion:** Bearbeiter = Person X (oder: „Gleichmäßig verteilen“ an Gruppe – Round Robin / geringste Auslastung)

### 2. Unteraufgaben bei Erstellung anlegen (Checkliste)
- **Auslöser:** Vorgang erstellt, Vorgangstyp = „Kundenauftrag“
- **Aktion:** Unteraufgaben erstellen: „Konstruktion“, „Stückliste“, „Bestellung“, „Montage“, „Inbetriebnahme“

### 3. Elternvorgang schließen, wenn alle Unteraufgaben fertig
- **Auslöser:** Vorgang übergegangen nach „Erledigt“
- **Bedingung:** Vorgangstyp = Unteraufgabe; Verwandte Vorgänge: Unteraufgaben des Elternvorgangs sind alle erledigt
- **Zweig:** Elternvorgang → **Aktion:** Übergang nach „Erledigt“

### 4. Epic in Arbeit setzen, sobald ein Vorgang startet
- **Auslöser:** Vorgang übergegangen nach „In Bearbeitung“
- **Zweig:** Epic (Elternvorgang) → **Bedingung:** Status = „Offen“ → **Aktion:** Übergang „In Bearbeitung“

### 5. Erinnerung bei überfälligen Vorgängen
- **Auslöser:** Geplant, täglich 08:00, JQL: `duedate < now() AND statusCategory != Done`
- **Aktion:** E-Mail/Teams-Nachricht an Bearbeiter: „{{issue.key}} – {{issue.summary}} ist seit {{issue.duedate.diff(now).days}} Tagen überfällig“

### 6. Kunde antwortet → zurück in Bearbeitung (JSM)
- **Auslöser:** Kommentar hinzugefügt
- **Bedingungen:** Kommentar ist öffentlich; Ersteller = Melder; Status = „Warten auf Kunde“
- **Aktion:** Übergang nach „In Bearbeitung“

### 7. Auto-Close nach Warten auf Kunde (JSM)
- **Auslöser:** Geplant, täglich, JQL: `status = "Warten auf Kunde" AND updated <= -5d`
- **Aktion:** Kommentar an Kunden („Wir schließen die Anfrage mangels Rückmeldung …“), Übergang „Gelöst“

### 8. Onboarding-Paket
- **Auslöser:** Vorgang erstellt, Request Type = „Neue Mitarbeiterin / neuer Mitarbeiter“
- **Aktionen:** Vorgänge in anderen Projekten erstellen (IT: Laptop & Konten, Facility: Arbeitsplatz, HR: Unterlagen), alle mit dem Ursprungsvorgang verknüpfen, Fälligkeit = `{{issue.customfield_XXXXX.minusBusinessDays(3)}}` (Startdatum-Feld)

### 9. Priorität aus Auswirkung × Dringlichkeit
- **Auslöser:** Vorgang erstellt
- **Bedingungen (if/else):** Auswirkung = „Ganze Firma“ UND Dringlichkeit = „Hoch“ → Priorität „Kritisch“ usw. (Matrix aus [Kapitel 05](05-jira-service-management.md))

### 10. Kritischer Vorgang → Sofortmeldung im Chat
- **Auslöser:** Vorgang erstellt
- **Bedingung:** Priorität = Kritisch
- **Aktion:** Microsoft-Teams- oder Slack-Nachricht an Kanal mit Link `{{issue.url}}`

### 11. Fälligkeitsdatum automatisch setzen
- **Auslöser:** Vorgang erstellt
- **Aktion:** Fälligkeitsdatum = `{{now.plusBusinessDays(5)}}`

### 12. Pflichtinfo fehlt → Vorgang zurückweisen
- **Auslöser:** Vorgang erstellt
- **Bedingung:** Feld „Seriennummer“ ist leer
- **Aktionen:** Kommentar an Melder „Bitte Seriennummer ergänzen“, Status „Warten auf Kunde“

### 13. Status synchronisieren über verknüpfte Vorgänge
- **Auslöser:** Vorgang übergegangen nach „Erledigt“
- **Zweig:** Verknüpfte Vorgänge (Typ „blockiert“) → **Aktion:** Kommentar „Blocker {{triggerIssue.key}} ist gelöst“

### 14. Wöchentlicher Bericht per Mail
- **Auslöser:** Geplant, montags 07:30
- **Aktion:** „Vorgänge nachschlagen“ (Lookup) mit JQL `project = SVC AND resolved >= -7d`
- **Aktion:** E-Mail an Leitung: „Letzte Woche gelöst: {{lookupIssues.size}}“ + Liste `{{#lookupIssues}}{{key}} – {{summary}}{{/}}`

### 15. Externe Daten holen (Webanfrage)
- **Auslöser:** Vorgang erstellt
- **Aktion:** Webanfrage senden (GET an Kunden-/ERP-API mit Kundennummer), **„Auf Antwort warten“** aktivieren
- **Aktion:** Feld bearbeiten: Kundenname = `{{webResponse.body.name}}`

### 16. Vorgang an externes System senden
- **Auslöser:** Vorgang übergegangen nach „Freigegeben“
- **Aktion:** Webanfrage POST an n8n-Webhook mit Body:
```json
{ "key": "{{issue.key}}", "summary": "{{issue.summary}}", "assignee": "{{issue.assignee.emailAddress}}" }
```

### 17. Doppelte Anfragen erkennen
- **Auslöser:** Vorgang erstellt
- **Aktion:** Lookup JQL: `project = SVC AND summary ~ "{{issue.summary}}" AND created >= -1d AND key != {{issue.key}}`
- **Bedingung:** `{{lookupIssues.size}}` > 0 → Label „moeglicher-duplikat“ setzen

### 18. Zeit bis Lösung in Feld schreiben
- **Auslöser:** Übergang nach „Erledigt“
- **Aktion:** Feld „Durchlaufzeit (Tage)“ = `{{issue.created.diff(now).businessDays}}`

### 19. Wiederkehrende Wartung anlegen
- **Auslöser:** Geplant, monatlich am 1.
- **Aktion:** Vorgang erstellen „Wartung Maschine X – {{now.format("MMMM yyyy")}}“ mit Unteraufgaben

### 20. KI-Zusammenfassung (falls Rovo/KI aktiv)
- **Auslöser:** Übergang nach „Gelöst“
- **Aktion:** KI-Aktion „Zusammenfassen“ → Kommentar intern, als Basis für Wissensartikel

---

## Smart-Values-Spickzettel

| Smart Value | Ergebnis |
|---|---|
| `{{issue.key}}` | z. B. SVC-123 |
| `{{issue.summary}}` | Zusammenfassung |
| `{{issue.url}}` | Link zum Vorgang |
| `{{issue.reporter.displayName}}` | Name des Melders |
| `{{issue.assignee.emailAddress}}` | Mail des Bearbeiters |
| `{{issue.status.name}}` | Statusname |
| `{{issue.customfield_10050}}` | Benutzerdefiniertes Feld (ID nachschlagen) |
| `{{now.plusBusinessDays(3)}}` | Datum in 3 Werktagen |
| `{{issue.created.diff(now).days}}` | Alter in Tagen |
| `{{triggerIssue.key}}` | Auslösender Vorgang (in Zweigen) |
| `{{lookupIssues.size}}` | Anzahl gefundener Vorgänge |
| `{{webResponse.body}}` | Antwort einer Webanfrage |
| `{{comment.body}}` | Text des Kommentars |
| `{{initiator.displayName}}` | Wer hat die Regel ausgelöst |

Feld-IDs findest du über die REST API: `GET /rest/api/3/field` (siehe [scripts](scripts/)).
