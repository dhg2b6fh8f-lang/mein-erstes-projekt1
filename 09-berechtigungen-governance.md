# 09 – Berechtigungen & Governance

## Prinzip: Gruppen → Projektrollen → Berechtigungsschema

```
Nutzer → Gruppe (z. B. jira-service-agents)
       → Projektrolle im Projekt (z. B. "Bearbeiter")
       → Berechtigungsschema vergibt Rechte an Rollen (nicht an Einzelpersonen!)
```

**Vorteil:** Ein Berechtigungsschema für viele Projekte; wer in welchem Projekt was darf, regelt der Projekt-Admin über die Rollen.

## Standard-Rollen

| Rolle | Darf |
|---|---|
| Administratoren | Projekt konfigurieren, alles im Projekt |
| Bearbeiter (Member) | Vorgänge erstellen, bearbeiten, übergehen, zuweisen, kommentieren |
| Betrachter (Viewer) | Nur lesen und kommentieren |
| Service Desk Team (JSM) | Agents, interne Kommentare |
| Service Desk Customers (JSM) | Nur eigene/organisationsweite Anfragen im Portal |

## Beispiel-Berechtigungsschema „Standard intern“

| Recht | Rollen |
|---|---|
| Projekt durchsuchen | Administratoren, Bearbeiter, Betrachter |
| Vorgänge erstellen | Administratoren, Bearbeiter |
| Vorgänge bearbeiten | Administratoren, Bearbeiter |
| Vorgänge zuweisen | Administratoren, Bearbeiter |
| Zuweisbarer Benutzer | Bearbeiter |
| Übergänge ausführen | Administratoren, Bearbeiter |
| Vorgänge löschen | **nur Administratoren** |
| Eigene Kommentare bearbeiten | alle mit Zugriff |
| Alle Kommentare löschen | nur Administratoren |
| Projekt verwalten | Administratoren |

## Vertrauliches: Sicherheitsstufen
Für HR, Geschäftsführung, Personalfälle: **Sicherheitsstufe** am Vorgang → nur bestimmte Gruppe/Rolle sieht ihn. Per Automation automatisch setzen (z. B. bei Request Type „Personalangelegenheit“).

## Admin-Ebenen in Jira Cloud

| Ebene | Wer | Aufgaben |
|---|---|---|
| Organisations-Admin | 1–2 Personen IT | Nutzer, Domänen, SSO, Abrechnung |
| Jira-Admin (Site) | Jira-Owner | Schemes, Felder, globale Einstellungen |
| Projekt-Admin | Teamleitung | Rollen, Komponenten, Boards im eigenen Projekt |

**Regel:** So wenige Site-Admins wie möglich (2 reichen, einer als Vertretung).

## Governance-Regeln (für den Kunden aufschreiben)
1. **Neue Felder** nur über den Jira-Owner, mit Begründung (Wofür? Wer pflegt es? Welcher Report?)
2. **Neue Projekte** auf Basis einer bestehenden Vorlage (gleiche Schemes)
3. **Änderungen an geteilten Workflows/Schemes** → erst in Sandbox/Testprojekt, Info an alle betroffenen Teams
4. **Automationen** mit Namenskonvention und verantwortlicher Person
5. **Quartalsweise aufräumen:** ungenutzte Felder, Filter, Boards, Automationen, inaktive Nutzer (Lizenzkosten!)
6. **Änderungsprotokoll** führen (Datum, Was, Wer, Warum)

## Sicherheits-Checkliste
- [ ] SSO und 2-Faktor-Authentifizierung aktiv
- [ ] Öffentlicher Zugriff (anonym) deaktiviert, außer bewusst gewollt
- [ ] Gruppe „Alle Nutzer“ nicht in Berechtigungen für sensible Projekte
- [ ] JSM: Wer darf sich im Portal selbst registrieren? (meist nur bestimmte Domains)
- [ ] API-Tokens: Nutzung dokumentiert, Service-Accounts mit minimalen Rechten
- [ ] Apps aus dem Marketplace: Datenzugriff und Hersteller geprüft
- [ ] Audit-Log regelmäßig ansehen
- [ ] Ausscheidende Mitarbeiter: Offboarding-Prozess deaktiviert Konto am letzten Tag
