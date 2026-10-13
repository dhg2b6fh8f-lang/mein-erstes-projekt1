# 17 – Dashboards (Stand 2026)

## Was es gibt
- **Klassische Dashboards** (Menü „Dashboards“): frei kombinierbare Gadgets, teilbar
- **Space-Dashboards** (seit Frühling 2026): ersetzen den alten Reiter „Berichte“ im Space, mit Diagrammen und Rovo-Auswertungen
- **„Für dich“-Seite:** persönliche Startseite mit zugewiesener Arbeit und Fristen
- **Kapazitätsansicht** (Sommer 2026): Auslastung im Team
- **JSM-Berichte:** SLA, Volumen, Zufriedenheit
- **Atlassian Analytics** (höhere Pläne): übergreifende Auswertungen mit SQL/Diagrammen
- **Marketplace-Apps** für Spezialfälle (z. B. erweiterte Diagramme, Checklisten-Auswertung)

## Eingebaute Gadgets (Auswahl, ca. 30 insgesamt)

| Gruppe | Gadgets |
|---|---|
| Persönlich | Mir zugewiesen, In Bearbeitung, Beobachtet, Aktivitäten |
| Filter-basiert | Filterergebnisse (Tabelle), Kreisdiagramm, Zweidimensionale Filterstatistik, Vorgangsstatistik |
| Trends | Erstellt vs. erledigt, Durchschnittsalter, Durchschnittliche Zeit im Status, Lösungszeit |
| Agil | Sprint-Zustand, Sprint-Burndown, Verbleibende Tage im Sprint, Roadmap |
| Service | Zeit bis zur ersten Antwort |
| Hilfen | Einführung (Text), Labels, Abstandhalter |

**Wichtig:** Die meisten Gadgets brauchen einen **gespeicherten Filter**. Filter einmal anlegen, mehrfach nutzen.

## Vorlagen nach Rolle

### Teamleitung Service (JSM)
```
┌───────────────────────────┬───────────────────────────┐
│ Zeit bis erste Antwort    │ Kreisdiagramm:            │
│ (Trend)                   │ Anfragen nach Request Type│
├───────────────────────────┼───────────────────────────┤
│ Filterergebnisse:         │ 2D-Statistik:             │
│ SLA verletzt / läuft ab   │ Agent × Status            │
└───────────────────────────┴───────────────────────────┘
```
Filter: `"Time to resolution" = breached() AND statusCategory != Done`

### Projektleitung Kundenauftrag (Maschinenbau)
```
┌───────────────────────────┬───────────────────────────┐
│ Roadmap / Zeitachse       │ Filterergebnisse:         │
│ (Epics = Aufträge)        │ Überfällige Arbeitspakete │
├───────────────────────────┼───────────────────────────┤
│ 2D-Statistik:             │ Erstellt vs. erledigt     │
│ Auftrag × Status          │ (90 Tage)                 │
└───────────────────────────┴───────────────────────────┘
```

### Geschäftsführung
- Erstellt vs. erledigt (Wächst der Rückstau?)
- Durchschnittsalter offener Vorgänge
- Kreisdiagramm offene Vorgänge nach Bereich/Komponente
- JSM: SLA-Erfolgsquote, Zufriedenheit

### Mitarbeitende
- Mir zugewiesen
- Überfällig (eigene)
- Beobachtet

### Softwareteam
- Sprint-Zustand, Burndown
- Bug-Trend (Erstellt vs. erledigt, nur Bugs)
- Offene Bugs mit hoher Priorität
- Status × Bearbeiter (Überlastung erkennen)

## Regeln für gute Dashboards
1. **Ein Dashboard = eine Zielgruppe = eine Frage/Entscheidung.** Nicht „alles für alle“.
2. **Max. ca. 6 Gadgets.**
3. **Sprechende Namen**, z. B. „Service – Tagesübersicht Teamleitung“.
4. **Gespeicherte Filter** hinter den Gadgets statt fest eingetippter JQL – eine Änderung wirkt überall.
5. **Verantwortliche Person** in der Beschreibung nennen.
6. **Ein Gadget nach dem anderen** bauen und prüfen.
7. Status-Gadget mit **Qualitäts-Gadget** kombinieren (Bewegt sich die Arbeit *und* ist sie wirklich fertig?).
8. Für Leute ohne Jira-Zugang: Diagramm per **Jira-Makro in Confluence** teilen.

## Typische Stolperfallen
- **Leere Gadgets** für andere Nutzer: Sie haben keine Rechte auf den Filter oder das Projekt. Dashboard- und Projektrechte sind getrennt – beides teilen.
- **Öffentlich teilen** zeigt nur Vorgänge aus öffentlichen Projekten.
- **Free-Plan** hat Einschränkungen beim Teilen.
- Jira kann **keine Checklisten-Inhalte** in Vorgängen auswerten – nur den Status. Dafür braucht es Apps.
- Aktualisierung standardmäßig etwa alle **15 Minuten**. Kürzere Intervalle bei vielen Gadgets belasten das System.
- **Seit Frühling 2026** sind Sprint-Reports über Space-Dashboards erreichbar – Nutzer suchen sie anfangs. Schulung anpassen.

## Kennzahlen mit Bedeutung
Siehe auch [Kapitel 10](10-reporting-jql.md).

| Frage der Leitung | Gadget / Kennzahl |
|---|---|
| Schaffen wir die Arbeit? | Erstellt vs. erledigt |
| Wie schnell sind wir? | Lösungszeit, Durchschnittliche Zeit im Status |
| Halten wir Zusagen ein? | SLA-Erfolgsquote |
| Wo stockt es? | Durchschnittliche Zeit im Status, Zweidimensionale Statistik Status × Bereich |
| Wer ist überlastet? | Kapazitätsansicht, 2D-Statistik Bearbeiter × Status |
| Sind Kunden zufrieden? | JSM-Zufriedenheit |

> **Betriebsrat:** Auswertungen pro Person (z. B. „wer hat wie viel erledigt“) können mitbestimmungspflichtig sein. Lieber Teamzahlen zeigen.
