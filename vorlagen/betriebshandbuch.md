# Betriebshandbuch – Jira bei <Firmenname>

**Jira-Owner:** <Name> · **Vertretung:** <Name> · **Externer Support:** <Dein Name, Kontakt>
**Stand:** <Datum>

## 1. Überblick
- Site: <firma>.atlassian.net
- Produkte & Plan: <…>
- Projekte: <Liste mit Schlüssel und Zweck>

## 2. Konfiguration (Kurzfassung des Konzepts)
- Workflows: <Name – genutzt von – Besonderheiten>
- Wichtige Felder: <…>
- Schemes: <…>

## 3. Automationen
| Name | Was sie tut | Verantwortlich | Bei Fehler |
|---|---|---|---|
| | | | |

## 4. Integrationen
| System | Technik | Technischer Nutzer | Wo liegt das Token? | Ansprechpartner |
|---|---|---|---|---|
| | | | (Passwortmanager – nie im Klartext hier!) | |

## 5. Standardaufgaben
### Neue Person anlegen
1. admin.atlassian.com → Benutzer → Einladen
2. Gruppe(n) zuweisen: <…>
3. Ggf. Projektrolle setzen

### Person ausscheiden
1. Offene Vorgänge neu zuweisen (`assignee = <Person> AND statusCategory != Done`)
2. Benutzer deaktivieren (spart Lizenz)

### Neues Projekt nach Vorlage
1. Projekt erstellen → „Konfiguration von bestehendem Projekt übernehmen“ → <Vorlageprojekt>
2. Projekt-Admin und Rollen setzen

### Neuer Wert in Auswahlliste
Einstellungen → Vorgänge → Benutzerdefinierte Felder → <Feld> → Kontexte → Werte bearbeiten

## 6. Governance-Regeln
Siehe Kapitel 09 des Playbooks – hier die vereinbarten Regeln eintragen.

## 7. Änderungsprotokoll
| Datum | Änderung | Wer | Warum |
|---|---|---|---|
| | | | |

## 8. Notfall
- Atlassian-Status: status.atlassian.com
- Atlassian-Support: support.atlassian.com (je nach Plan)
- Externer Support: <Kontakt, Reaktionszeit laut Wartungsvertrag>
