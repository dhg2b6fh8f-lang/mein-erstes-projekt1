# 09 – Pipeline & Kennzahlen

## Vertriebs-Pipeline in Jira (dein eigenes Werkzeug nutzen!)
Ein eigenes Jira (Free-Plan, bis 10 Nutzer) als CRM – gleichzeitig Übung und Vorzeigeobjekt für Kunden.

### Space „Vertrieb“ (Kanban)
**Vorgangstyp:** „Lead“ / „Chance“

**Workflow (Spalten):**
```
Kontakt → Erstgespräch vereinbart → Erstgespräch geführt → Angebot gesendet → Verhandlung → Gewonnen
                                                                                       ↘ Verloren
                                                                                       ↘ Später (Wiedervorlage)
```

**Felder:**
| Feld | Typ | Zweck |
|---|---|---|
| Firma | Text | |
| Ansprechperson / Rolle | Text | |
| Quelle | Auswahl: Netzwerk, Empfehlung, LinkedIn, Event, Brief, Plattform, Partner, Website | Welcher Kanal funktioniert? |
| Kontakterlaubnis | Auswahl: E-Mail erlaubt, Nur Telefon nach Kontakt, Nur LinkedIn, Sperren | Rechtssicher bleiben |
| Erwarteter Wert (€) | Zahl | Pipeline-Wert |
| Wahrscheinlichkeit (%) | Zahl | Prognose |
| Nächster Schritt | Text | Immer gefüllt! |
| Fälligkeitsdatum | Datum | Wiedervorlage |
| Verlustgrund | Auswahl: Preis, Timing, Kein Bedarf, Anderer Anbieter, Kein Entscheider, Keine Antwort | Lernen |

**Automationen (sparsam, Free = 150 Schritte/Monat):**
- Täglich: Erinnerung an Leads mit überfälligem „Nächster Schritt“
- Bei „Gewonnen“: Projekt-Epic im Lieferungs-Space anlegen

**Dashboard:** Leads pro Phase · Pipeline-Wert · Gewonnen/Verloren nach Quelle · Überfällige Wiedervorlagen

## Kennzahlen (monatlich ansehen)

| Kennzahl | Formel | Gut für |
|---|---|---|
| Neue Kontakte | Anzahl | Aktivität |
| Erstgespräche | Anzahl | Wichtigste Frühkennzahl |
| Gespräch → Angebot | Angebote / Gespräche | Qualität der Gespräche & Leads |
| Abschlussquote | Gewonnen / Angebote | Qualität der Angebote |
| Durchschnittlicher Auftragswert | Umsatz / Aufträge | Preisgestaltung |
| Verkaufsdauer | Tage von Erstkontakt bis Auftrag | Planung |
| Umsatz nach Quelle | Summe je Kanal | Wo Zeit investieren? |
| Wiederkehrender Umsatz | Summe Wartungsverträge/Monat | Stabilität |

**Rückwärts rechnen:** Ziel 2 Aufträge pro Monat, Abschlussquote 40 % → 5 Angebote → bei 50 % Gespräch-zu-Angebot → **10 Erstgespräche pro Monat** nötig.

## Wöchentlicher Pipeline-Check (15 Min.)
1. Hat jeder offene Lead einen **nächsten Schritt mit Datum**?
2. Was ist überfällig? → heute erledigen
3. Welche Leads hängen seit > 30 Tagen? → nachfassen oder auf „Später“
4. Reicht die Pipeline für die nächsten 2 Monate? Wenn nicht → mehr Akquise
