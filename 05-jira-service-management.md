# 05 – Jira Service Management (JSM)

JSM = Jira für Service-Teams: Kunden (intern oder extern) stellen Anfragen über ein Portal oder per E-Mail, Agents bearbeiten sie in Queues mit SLAs.

## Bausteine

| Baustein | Was es ist | Tipp |
|---|---|---|
| **Portal** | Webseite für Kunden zum Anfragen stellen | Klar benannte Kategorien, Kundensprache statt IT-Sprache |
| **Request Type** | Anfrageart im Portal (z. B. „Laptop bestellen“) | Basiert auf einem Vorgangstyp, eigene Felder/Texte |
| **Queue** | Gefilterte Liste für Agents | Nach Priorität/SLA sortieren, max. 8–10 Queues |
| **SLA** | Zeitziel (Erste Antwort, Lösung) | Mit Kalender (Geschäftszeiten, Feiertage NRW etc.) |
| **Kunden & Organisationen** | Wer anfragen darf | Organisationen = Firmen/Abteilungen |
| **E-Mail-Kanal** | Mail an Postfach → Ticket | Microsoft 365/Google per OAuth verbinden |
| **Wissensdatenbank** | Confluence-Bereich mit Artikeln | Portal schlägt Artikel vor → weniger Tickets |
| **Assets** | Inventar (Maschinen, Laptops, Lizenzen) | Premium/Enterprise, Objekte mit Tickets verknüpfen |
| **Approvals** | Freigaben im Workflow | Für Bestellungen, Changes, Zugänge |

## Aufbau-Reihenfolge

1. Service-Projekt anlegen (Vorlage: IT Service Management, Kundenservice, HR, Facilities…)
2. Vorgangstypen & Workflows festlegen ([Kapitel 04](04-workflow-design.md))
3. Request Types anlegen, Felder und Hilfetexte formulieren
4. Portal-Gruppen (Kategorien) strukturieren
5. Kalender + SLAs definieren
6. Queues bauen
7. E-Mail-Kanal verbinden
8. Kunden/Organisationen und Berechtigungen (Wer darf Tickets stellen? Wer sieht wessen Tickets?)
9. Wissensdatenbank anbinden
10. Automation (Zuweisung, Erinnerungen, Auto-Close) – siehe [Kapitel 06](06-automation-rezepte.md)
11. Reports/Dashboards (SLA-Einhaltung, Volumen, Zufriedenheit)

## SLA-Beispiele

| SLA | Start | Pause | Stopp | Ziel (Beispiel) |
|---|---|---|---|---|
| Zeit bis erste Antwort | Ticket erstellt | – | Kommentar für Kunde | Hoch 2 h, Mittel 8 h, Niedrig 24 h |
| Zeit bis Lösung | Ticket erstellt | Status „Warten auf Kunde“ | Status „Gelöst“ | Hoch 1 Tag, Mittel 3 Tage, Niedrig 5 Tage |

Immer mit **Geschäftszeiten-Kalender** arbeiten, sonst laufen SLAs nachts und am Wochenende.

## ITSM-Praktiken (ITIL-orientiert)

| Praxis | Vorgangstyp | Kern |
|---|---|---|
| Service Request | Serviceanfrage | Standardanfragen mit festem Ablauf |
| Incident | Störung | Schnelle Wiederherstellung, Priorität = Auswirkung × Dringlichkeit |
| Problem | Problem | Ursachenanalyse für wiederkehrende Störungen |
| Change | Änderung | Risikobewertung + Freigabe vor Umsetzung |
| Post-Incident Review | – | Lernen aus großen Störungen |

**Prioritätsmatrix (Beispiel):**

| Auswirkung ↓ / Dringlichkeit → | Hoch | Mittel | Niedrig |
|---|---|---|---|
| Ganze Firma | Kritisch | Hoch | Mittel |
| Abteilung | Hoch | Mittel | Niedrig |
| Einzelperson | Mittel | Niedrig | Niedrig |

## Typische JSM-Einsatzfälle bei KMU
- **IT-Helpdesk** (Passwort, Hardware, Software, Zugänge)
- **Kundenservice / Maschinen-Service** (Störungsmeldung, Ersatzteilanfrage, Wartungstermin)
- **HR-Service** (Bescheinigungen, Onboarding, Urlaub-Sonderfälle) – Sicherheitsstufen beachten
- **Facility** (Reparatur, Raum, Schlüssel)
- **Einkauf** (Bestellanforderung mit Freigabe nach Betrag)

## Kundenportal-Texte – Regeln
- Request-Type-Namen als Aufforderung: „Störung an Maschine melden“, „Ersatzteil anfragen“
- Kurzer Hilfetext: Was passiert danach? Wie schnell?
- Nur Felder abfragen, die der Agent wirklich braucht
- Seriennummer/Maschinentyp als Auswahl oder Assets-Feld statt Freitext
