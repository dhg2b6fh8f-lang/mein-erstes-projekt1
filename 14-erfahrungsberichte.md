# 14 – Erfahrungsberichte von Unternehmen und Praktikern

Gesammelt aus Fallstudien, Atlassian-Konferenzen, der Atlassian Community, Bewertungsportalen (Capterra, GetApp) und Fachblogs. Alle Inhalte sind sinngemäß zusammengefasst. Quellen: [Quellenverzeichnis](quellen.md).

> **Vorsicht bei Zahlen:** Viele Fallstudien stammen von Atlassian oder Partnern, die daran verdienen. Die Ergebnisse sind nicht unabhängig geprüft. Sie zeigen aber gut, *was* funktioniert hat.

---

## Teil A – Unternehmens-Fallstudien

### 1. Siemens Energy – Außendienst raus aus Excel
- **Ausgangslage:** Der Service für Dampfturbinen lief über Tabellen, Papierformulare und E-Mail-Ketten. Eine verpasste Übergabe konnte teure Verzögerungen auslösen.
- **Lösung:** Mit einem Implementierungspartner wurde der komplette Außendienst-Prozess in Jira Service Management neu aufgebaut, danach mit Automation und Rovo ergänzt.
- **Ergebnis (laut Atlassian):** Arbeit läuft etwa dreimal schneller, jede Übergabe ist nachvollziehbar.
- **Lehre für dich:** Genau das Szenario deiner Zielkunden (Maschinen-/Anlagenbau). Das Verkaufsargument heißt **„keine verlorenen Übergaben mehr“**, nicht „modernes Tool“.

### 2. Fidelity Investments – 99 % weniger Anpassungen
- **Ausgangslage:** Rund 30.000 Nutzer, 5.000 Jira-Projekte, über Jahre gewachsener Wildwuchs.
- **Lösung:** Radikale Vereinheitlichung: **ein** Workflow, **12** Status, **unter 100** benutzerdefinierte Felder.
- **Ergebnis:** Bessere Performance und Bedienbarkeit.
- **Lehre:** Selbst ein Konzern kommt mit einem Workflow aus. Bei KMU erst recht: **Weniger ist mehr.**

### 3. VistaPrint – 20 Services in einem System
- **Ausgangslage:** Über 4.600 Mitarbeitende, 22 Standorte, über 4.000 Tickets pro Monat, altes Service-Tool, das kaum jemand nutzte.
- **Lösung:** Mehr als 20 getrennte Services in einem Service Desk zusammengeführt.
- **Ergebnis:** Ausrollen von 2 auf 22 Standorte in 5 Wochen, komplette Einführung in rund 2 Monaten, gute Akzeptanz.
- **Lehre:** Ein zentrales Portal statt vieler Postfächer ist ein starkes, schnell sichtbares Ergebnis.

### 4. Saint-Gobain – Wechsel von ServiceNow zu JSM
- **Lösung:** Die gesamte IT und die Hälfte der Endnutzer wurden in wenigen Wochen auf JSM umgestellt.
- **Ergebnis (laut Atlassian):** Rund 70 % geringere Kosten im ersten Jahr.
- **Lehre:** Kosten sind ein Hauptgrund für Wechsel weg von teuren ITSM-Suiten.

### 5. Globales Logistikunternehmen – 15 Jahre ServiceNow abgelöst
- **Problem:** Das System war so stark angepasst, dass Pflege aufwendig wurde. Man zahlte für ungenutzte Funktionen. Eine Wissensdatenbank mit über 10.000 Seiten schreckte lange vom Wechsel ab.
- **Vorgehen:** Das interne Admin-Team machte die Hauptarbeit, ein Partner beriet, schrieb Skripte für Sonderrechte und migrierte die Wissensdatenbank samt Links und Anhängen.
- **Ergebnis:** Start im Zeitplan, deutlich weniger Pflegeaufwand, geringere Lizenzkosten.
- **Lehre:** Kunden wollen oft selbst mitarbeiten. **Beratung + Spezialaufgaben** ist ein realistisches Modell für dich.

### 6. Indeed – Data Center → Cloud
- **Umfang:** Rund 11.000 Jira-Nutzer, 4 Mio. Vorgänge, 15.000 Confluence-Nutzer.
- **Vorgehen:** Bewusst „erst umziehen, dann aufräumen“. Inaktive Projekte archiviert, jeder Schritt in **Proben** gestoppt, Ziel war ein Umstieg in 48 Stunden. Wöchentlicher Lenkungskreis, 5 Tage Rund-um-die-Uhr-Support danach.
- **Lehren:** Proben sind entscheidend. Kommunikation, Schulung und Support sind genauso wichtig wie die Technik. Ein Plan muss die ganze Zeit abdecken, nicht nur das Umzugswochenende.

### 7. Migration mit Marketplace-App-Daten (Hersteller-Fallstudie)
- **Problem:** Nach der Migration fehlten bei manchen Vorgängen App-Daten (Checklisten). Ursache: ein Fehler im Export-Skript, der Daten in größeren Wellen übersprang. Zusätzlich entstanden doppelte Felder durch Migration in mehreren Wellen.
- **Lösung:** Fehler gefunden durch ausführliches Logging, betroffene Welle neu migriert, doppelte Felder zusammengeführt.
- **Lehren:** In Wellen migrieren, nach **jeder** Welle Daten zählen und vergleichen, Zeit fürs Aufräumen danach einplanen.

### 8. US-Versicherer – Migration in 3 Monaten
- **Lehren:** Infrastruktur-Teams (Netzwerk, Speicher) **früh** einbinden, weil die eigene Warteschlangen haben – eine verzögerte Netzwerkänderung kostete Wochen. Jede Änderung (Apps, Felder, Prozesse) über einen Freigabeprozess.

### 9. NGO verlässt Jira (Gegenbeispiel)
- **Grund:** Das Ende von Jira Server zwang zur Entscheidung. Cloud war zu teuer, und bei Gesundheitsdaten wollte man die Daten selbst kontrollieren. Wechsel zu einem selbst gehosteten Open-Source-Tool.
- **Lehre:** **Kosten und Datenschutz** sind echte Ausstiegsgründe. Bei sensiblen Daten früh über Datenresidenz und Alternativen sprechen.

### 10. Assets/CMDB-Beispiele (laut Atlassian)
- Eine Hochschule senkte falsch zugeordnete Anfragen um rund 80 % durch eine saubere Asset-Struktur.
- Ein Konzern verkleinerte vor dem Neuaufbau gemeinsam mit den Fachbereichen bewusst den Umfang der erfassten Assets.
- **Lehre:** Bei Assets klein anfangen, Datenmodell zuerst, dann automatisieren.

---

## Teil B – Was Praktiker in der Community berichten

### Erfolgreiche Einführungen haben gemeinsam
1. **Dashboards pro Rolle** fördern die Nutzung stärker als ausgefeilte JQL.
2. **Eine verantwortliche Person oder ein Team** für das System.
3. **Erst Prozess, dann Tool** – und vor der Konfiguration klären, was „fertig“ heißt.
4. **Wenige Standard-Workflow-Schemes** (z. B. einfach, Softwareentwicklung, Anfragen).
5. **Gelenkte Freiheit:** Leitplanken und ein paar freigegebene Varianten statt totaler Freiheit oder totaler Starre.
6. **Wenige Admins**, die gleichzeitig schulen und Best Practices vorleben.
7. **Pilot-Team zuerst**, dann nach festem Plan weitere Teams.
8. **Testumgebung** für Änderungen.
9. **Regelmäßige Reviews**: z. B. 30 Tage nach Go-Live – das ist viel billiger als Probleme nach 6 Monaten zu reparieren.
10. **Gute Vorgangsinhalte**: Nutzer schulen, klare Zusammenfassungen und Beschreibungen zu schreiben.

### Gescheiterte Einführungen haben gemeinsam
1. **Jedes Team eigene Workflows, Felder, Boards** – Wechsel zwischen Teams und Administration werden schwer.
2. **Ungeschulte oder zu viele Admins** – schnelle Änderungen erzeugen technische Schulden.
3. **Zu komplex**: viele Vorgangstypen, viele Status.
4. **Feld-Wildwuchs**: zu viele, doppelte, ungenutzte Felder.
5. **Workflows umgangen**: Vorgänge werden erledigt, ohne den Status zu ändern – niemand kennt den echten Stand.
6. **Kommentare statt Felder** für Anforderungsänderungen.
7. **Projekte einfach kopiert**, ohne die Anforderungen zu klären.
8. **Labels ohne Wörterbuch** – Tippfehler und Varianten machen Filter unbrauchbar.
9. **Verwaiste Vorgänge und Projekte** von Leuten, die das Unternehmen verlassen haben.
10. **Widerstand** besonders bei langjährigen Mitarbeitenden.

### Elf typische Fehler laut Experteninterview
1. Konfiguration als „vorläufig“ behandeln – später ist sie kaum noch änderbar.
2. Für jede Ausnahme ein eigenes Feld oder einen eigenen Workflow-Pfad bauen.
3. Jira nur als „Ticket-Eimer“ nutzen – unzuverlässige Daten.
4. Unklare Rechte (mal alles offen, mal alles zu).
5. Zu komplexe Workflows.
6. Irreführende Reports auf Basis von optionalen oder falsch genutzten Feldern.
7. **Kaputte Prozesse automatisieren** – Automation versteckt dann die Probleme.
8. Jira zu CRM oder ERP umbauen – besser spezialisierte Tools integrieren.
9. Nur **ein** Admin – Engpass und Ausfallrisiko.
10. Kulturprobleme als Technikprobleme tarnen.
11. Dashboards als Dekoration statt für konkrete Entscheidungen.

### Größte Zeitfresser laut Admins
- **Konfigurationsschulden:** Viele kleine Änderungen (ein Feld hier, ein Status da, eine schnelle Regel) wirken über die Zeit zusammen und werden unüberschaubar. Lösung: Architektur vereinfachen statt Symptome flicken.
- **Unkoordinierte Änderungen** mehrerer Beteiligter in derselben Instanz. Lösung: Regeln, stabile Schemes, Wiederverwendung, eingeschränkter Zugang.
- **Feld-Wildwuchs** in einer geerbten Instanz. Lösung, die funktioniert hat: alle Felder in einer Liste erfassen (Nutzung, letztes Verwendungsdatum, Optionen), Fachbereiche markieren „behalten/löschen“, behaltene Felder allgemeiner machen.
- **Team-managed Projekte** gelten als Governance-Albtraum, weil jedes Team eigene Felder anlegen kann.

---

## Teil C – Was Nutzer in Bewertungen sagen

### Jira Service Management (Capterra, Firmen von 1 bis 10.000+ Mitarbeitenden)
**Gelobt:**
- Zusammenspiel mit Confluence und Jira (häufigster Auswahlgrund)
- Workflows, Queues, SLAs, Automation – ein Nutzer schätzt rund 30 % Zeitersparnis bei Zuordnung und Nachverfolgung
- Wissensdatenbank im Portal
- Support-Team von Atlassian

**Kritisiert:**
- Steile Lernkurve (häufigste Kritik)
- Viel Einrichtungsaufwand, Standard ist sehr einfach
- Kosten für kleine Firmen, vor allem mit Apps
- **Lizenzfalle:** Nutzer wurden automatisch als zahlende Plätze hinzugefügt
- Zeitweise langsam
- Für Anfragende schwer, eigene Tickets zu verfolgen

**Tipps der Nutzer:** Zeit und Know-how für die Erstkonfiguration einplanen. Nutzer-Bereitstellung und Lizenzeinstellungen früh prüfen. App-Kosten mitrechnen.

### Jira (Capterra, GetApp – auch deutsche Bewertungen)
**Gelobt:** Agile Boards, flexible Workflows, Integrationen (GitHub, Slack), Skalierung, Reporting.
**Kritisiert:** Überladene Oberfläche, Suche nach Vorgängen mühsam, starr bei schnell wechselnden Prozessen, hoher Einrichtungsaufwand, zu viel Aufwand für einfache Aufgaben, Performance bei großen Projekten.
**Wechsel zu Jira** kommen oft von Asana, Trello, ClickUp, monday.com, Redmine – wegen besserer Agile-Unterstützung und mehr Funktionen.

---

## Was das für deine Beratung heißt

| Erkenntnis | Dein Angebot |
|---|---|
| Komplexität ist die Hauptkritik | „Schlanke Jira-Einführung“: max. 5–7 Status, wenige Pflichtfelder |
| Einrichtung kostet Zeit | Festpreis-Pakete mit klarem Umfang |
| Feld-Wildwuchs in bestehenden Instanzen | **„Jira-Aufräum-Paket“** (Health Check + Bereinigung) |
| Lizenzfallen, Kosten | Lizenz-Check als Teil jedes Projekts |
| Automation wird ab 03.12.2026 nach Schritten abgerechnet | **„Automation-Audit“** – siehe [Kapitel 16](16-aktuelle-updates.md) |
| Schulung wird vernachlässigt | Rollen-Schulungen fest im Paket |
| Data Center endet 2029 | Migrationsberatung |
| KI-Agents brauchen saubere Daten | „KI-Readiness“: Felder, Komponenten, Prioritäten sauber machen |
