# 04 – Workflow-Design

## Grundregeln

1. **Status = Zustand, nicht Person.** „Wartet auf Freigabe“ statt „Bei Herrn Müller“.
2. **5–7 Status reichen fast immer.** Jeder Status braucht einen Grund (eigene Queue, eigener Report, eigene Verantwortung).
3. **Jeder Status gehört zu einer Kategorie** (To Do / In Progress / Done).
4. **Rückwege einplanen** (z. B. „Zurück in Bearbeitung“), sonst bauen Nutzer Workarounds.
5. **Lösung setzen** beim Wechsel in einen Done-Status (Post-Function oder Screen).
6. **Pflichtangaben an der Transition prüfen** (Validator), nicht über überall-Pflichtfelder.
7. **Einen Workflow für ähnliche Vorgangstypen teilen.**

## Bausteine einer Transition

| Baustein | Zweck | Beispiel |
|---|---|---|
| **Bedingung** | Wer darf die Transition sehen? | Nur Gruppe `jira-service-leitung` darf „Freigeben“ |
| **Validator** | Ist alles da? | Feld „Ursache“ muss gefüllt sein vor „Erledigt“ |
| **Post-Function** | Was passiert danach automatisch? | Lösung = „Erledigt“, Bearbeiter = aktueller Nutzer |
| **Screen** | Eingabemaske während der Transition | Kommentar + Lösung beim Schließen |

## Standard-Workflows (Vorlagen)

### A. Einfache Aufgabe
```
Offen → In Bearbeitung → Erledigt
          ↑______________|
```

### B. Aufgabe mit Freigabe
```
Offen → In Bearbeitung → In Prüfung → Erledigt
              ↑_______________| (Rückgabe)
```

### C. Software-Entwicklung
```
Backlog → Ausgewählt → In Arbeit → Code Review → Test → Fertig
                          ↑____________|___________|
```

### D. Service-Anfrage (JSM)
```
Offen → In Bearbeitung → Warten auf Kunde → In Bearbeitung → Gelöst → Geschlossen
                     ↘ Warten auf Dritte ↗
```
„Warten auf Kunde“ pausiert typischerweise die SLA-Uhr.

### E. Kundenauftrag (Maschinen-/Anlagenbau)
```
Angelegt → Konstruktion → Beschaffung → Fertigung/Montage → Inbetriebnahme → Abnahme → Abgeschlossen
```
Hier oft besser: **Epic = Auftrag**, Phasen als Vorgänge mit einfachem Workflow A – dann sieht man parallele Arbeit.

### F. Reklamation / RMA
```
Gemeldet → Prüfung → [Anerkannt | Abgelehnt] → Reparatur/Ersatz → Rückversand → Abgeschlossen
```
Validator: „Fehlerursache“ und „Maßnahme“ Pflicht vor Abschluss (wichtig für ISO 9001/8D).

### G. Change (ITSM)
```
Beantragt → Bewertung → Freigabe (Approval) → Geplant → In Umsetzung → Überprüft → Abgeschlossen
                                    ↘ Abgelehnt
```

### H. Onboarding
Ein Vorgang „Onboarding Max Mustermann“ + Automation, die Unteraufgaben für IT, Facility, HR, Teamleitung anlegt (siehe [Rezept 8](06-automation-rezepte.md)).

## Checkliste vor Freigabe eines Workflows
- [ ] Jeder Status hat eine Kategorie
- [ ] Jeder Done-Status setzt die Lösung
- [ ] Rückwege vorhanden
- [ ] Bedingungen/Validatoren getestet (mit Test-Nutzer ohne Admin-Rechte!)
- [ ] Board-Spalten passen zu den Status
- [ ] Benachrichtigungen geprüft (nicht zu viele Mails)
- [ ] Workflow im Konzept dokumentiert
