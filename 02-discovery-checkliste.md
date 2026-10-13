# 02 – Discovery-Checkliste

Fragen für Erstgespräch und Workshops. Nicht alle Fragen in jedem Projekt – Abschnitte nach Bedarf wählen.

## A. Unternehmen & Ziele
- [ ] Branche, Größe, Standorte
- [ ] Welches Problem soll Jira lösen? (in den Worten des Kunden notieren)
- [ ] Woran merkt ihr in 3 Monaten, dass es erfolgreich war? (messbare Ziele)
- [ ] Wer entscheidet? Wer bezahlt? Wer wird täglich damit arbeiten?
- [ ] Zeitrahmen, Budget, feste Termine (Messe, Audit, Geschäftsjahr)

## B. Nutzer & Organisation
- [ ] Anzahl Nutzer gesamt / je Abteilung
- [ ] Interne Nutzer vs. externe (Kunden, Lieferanten, Partner)
- [ ] Welche Rollen gibt es? (Bearbeiter, Leitung, Freigeber, nur Lesen)
- [ ] Wie technisch affin sind die Nutzer?
- [ ] Gibt es Vertretungsregeln, Schichten, Rufbereitschaft?

## C. Prozesse (je Prozess wiederholen)
- [ ] Name des Prozesses, Auslöser (Wer/was startet ihn?)
- [ ] Schritte von Anfang bis Ende
- [ ] Wer macht welchen Schritt? Wo sind Übergaben?
- [ ] Welche Informationen braucht jeder Schritt (Pflichtangaben)?
- [ ] Entscheidungen / Freigaben (Wer? Nach welchen Kriterien?)
- [ ] Fristen, Eskalationen, Prioritäten
- [ ] Wie viele Fälle pro Woche/Monat?
- [ ] Was läuft heute schief? Wo geht Zeit verloren?
- [ ] Ausnahmen und Sonderfälle

**Typische Prozesse:** Kundenaufträge/Projekte, Service-/Supportanfragen, Reklamationen (RMA), Wartung/Instandhaltung, IT-Anfragen, Onboarding/Offboarding, Einkauf/Bestellfreigabe, Änderungsanträge (Change), Softwareentwicklung.

## D. Ist-Tools & Daten
- [ ] Was wird heute genutzt? (E-Mail, Excel, Trello, Asana, altes Ticketsystem, Jira Data Center…)
- [ ] Welche Daten sollen übernommen werden? Wie alt? Wie sauber?
- [ ] Anhänge, Kommentare, Historie nötig?
- [ ] Bestehende Atlassian-Produkte? (Confluence, Bitbucket, Data Center-Lizenzen)

## E. Integrationen
- [ ] E-Mail (Ticket per Mail erstellen? Welches Postfach – Microsoft 365, Google?)
- [ ] Chat (Teams, Slack)
- [ ] Login (Microsoft Entra ID / Google – SSO gewünscht?)
- [ ] ERP / CRM / Warenwirtschaft (SAP, Microsoft Dynamics, HubSpot, Salesforce…)
- [ ] Code-Hosting (GitHub, GitLab, Bitbucket)
- [ ] Dokumentation (Confluence, SharePoint)
- [ ] Zeiterfassung, Abrechnung
- [ ] KI-Nutzung gewünscht? (Rovo, Claude/ChatGPT über MCP)

## F. Reporting
- [ ] Welche Fragen soll das Management beantworten können?
- [ ] Welche Kennzahlen? (Durchlaufzeit, offene Fälle, SLA-Einhaltung, Auslastung)
- [ ] Wer sieht welche Reports? Wie oft?

## G. Sicherheit, Recht & Compliance
- [ ] DSGVO: Personenbezogene Daten in Tickets? Löschfristen?
- [ ] Datenresidenz in der EU gewünscht/vorgeschrieben? (Verfügbarkeit je Plan prüfen)
- [ ] Vertrauliche Bereiche (Personal, Geschäftsführung) → Sicherheitsstufen
- [ ] Betriebsrat einbinden? (Leistungs-/Verhaltenskontrolle durch Auswertungen möglich)
- [ ] Branchenvorgaben (ISO 9001, ISO 27001, Medizinprodukte, Cyber Resilience Act)
- [ ] Auftragsverarbeitungsvertrag (AVV/DPA) mit Atlassian nötig?

## H. Lizenz & Betrieb
- [ ] Cloud oder Data Center? (Hinweis: Data Center ist für Neukunden nicht mehr erhältlich, siehe [Kapitel 03](03-architektur-grundlagen.md))
- [ ] Plan: Free / Standard / Premium / Enterprise
- [ ] Wer ist künftig Jira-Admin beim Kunden?
- [ ] Wartungsvertrag gewünscht?

---

## Ergebnis der Discovery
Am Ende sollten feststehen:
1. Liste der Prozesse mit Priorität (was zuerst?)
2. Prozessbild je Prozess
3. Rollen- und Nutzerliste
4. Liste der Integrationen
5. Migrationsumfang
6. Offene Fragen und Risiken
