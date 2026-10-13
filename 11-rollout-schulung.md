# 11 – Rollout, Schulung & Adoption

Jira scheitert selten an der Technik, sondern daran, dass Leute weiter mit E-Mail und Excel arbeiten.

## Rollout-Strategien

| Strategie | Wann | Risiko |
|---|---|---|
| **Pilot → schrittweise** (empfohlen) | Mehrere Teams/Prozesse | Gering |
| Big Bang (alle gleichzeitig) | Kleines Unternehmen, ein Prozess | Mittel–hoch |
| Parallelbetrieb | Nur kurz (max. 1–2 Wochen) | Doppelarbeit, Daten auseinander |

## Schulung je Rolle

| Rolle | Dauer | Inhalte |
|---|---|---|
| **Anfragende / Portal-Kunden** | 10 Min. (Video oder Spickzettel) | Anfrage stellen, Status sehen, antworten |
| **Bearbeiter / Agents** | 60–90 Min. | Board/Queue, Vorgang bearbeiten, Übergänge, Kommentare (intern/öffentlich), Filter, Benachrichtigungen |
| **Teamleitung** | 60 Min. | Dashboards, Reports, Prioritäten, Zuweisung, einfache JQL |
| **Projekt-Admin / Jira-Owner** | 2–4 Std. | Rollen, Komponenten, Automation, Governance-Regeln, Betriebshandbuch |

**Format:** Lieber 2× kurz (Einführung + nach 1 Woche Fragerunde) als 1× lang. Immer am **echten System mit echten Beispielen**, nicht mit Folien.

## Material
- **Spickzettel (1 Seite) je Rolle**: Die 5 wichtigsten Klicks, Links zu Filtern/Dashboards, Ansprechpartner
- **Kurze Bildschirmvideos** (2–3 Min.) für häufige Aufgaben
- **FAQ-Seite** in Confluence / Wissensdatenbank

## Champions
- In jedem Team 1 Person, die Jira mag und Kolleg:innen hilft
- Etwas mehr Schulung, direkter Draht zum Jira-Owner
- Sammeln Verbesserungswünsche

## Hypercare (2–4 Wochen nach Go-Live)
- Tägliche 15-Min.-Sprechstunde (oder Teams-Kanal)
- Schnelle kleine Anpassungen (Feld umbenennen, Filter bauen)
- Wöchentlicher Kurzbericht an den Kunden: Fragen, Änderungen, Nutzung

## Adoption messen
| Messgröße | JQL / Quelle |
|---|---|
| Aktive Nutzer | Admin → Nutzer → letzte Aktivität |
| Neue Vorgänge pro Woche | `created >= -7d` |
| Vorgänge ohne Bearbeiter | `assignee IS EMPTY AND statusCategory != Done` |
| Veraltete Vorgänge | `updated <= -14d AND statusCategory != Done` |
| Anfragen noch per Mail statt Portal | Stichprobe im Service-Postfach |

## Widerstand – und was hilft
| Aussage | Antwort |
|---|---|
| „Das ist mehr Arbeit als vorher“ | Unnötige Pflichtfelder/Status streichen, Automation einsetzen |
| „Ich finde nichts“ | Persönliche Filter und Dashboard einrichten |
| „Zu viele Mails“ | Benachrichtigungsschema ausdünnen, persönliche Einstellungen zeigen |
| „Excel war übersichtlicher“ | Listenansicht/Tabelle zeigen, Export erklären |
| „Wozu das alles?“ | Nutzen aus Discovery zeigen (z. B. nichts geht mehr verloren) |
