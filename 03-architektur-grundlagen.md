# 03 – Architektur & Grundlagen

## 1. Cloud oder Data Center?

**Für neue Projekte praktisch immer Cloud.** Atlassian beendet Data Center:

| Datum | Was passiert |
|---|---|
| 30.03.2026 | Keine neuen Data-Center-Lizenzen für Neukunden |
| 30.03.2028 | Keine Lizenzverkäufe/Erweiterungen mehr für Bestandskunden |
| 28.03.2029 | Data-Center-Abos laufen aus, Instanzen werden schreibgeschützt |

→ Kunden mit Data Center brauchen bis spätestens 2029 eine Migration. **Großes Geschäftsfeld** (siehe [Migration](08-migration.md)).

## 2. Cloud-Pläne (Jira)

| | Free | Standard | Premium | Enterprise |
|---|---|---|---|---|
| Nutzer | bis 10 | bis 100.000 | bis 100.000 | bis 100.000 |
| Speicher | 2 GB | 250 GB | unbegrenzt | unbegrenzt |
| Automation | 150 Schritte/Abo | 400 Schritte/Nutzer/Monat | 750 Schritte/Nutzer/Monat | 1.000 Schritte/Nutzer/Monat |
| Berechtigungen | eingeschränkt | voll | voll | voll |
| Sandbox | – | – | ✓ | ✓ |
| Erweiterte Roadmaps | – | – | ✓ | ✓ |
| Uptime-SLA | – | – | 99,9 % | 99,95 % |

**JSM:** Abrechnung pro Agent (Bearbeiter); Kunden, die über das Portal Anfragen stellen, sind kostenlos. Free-Plan mit wenigen Agents – aktuelle Grenze bei Atlassian prüfen.

**Faustregel für KMU:** Standard reicht meistens. Premium lohnt sich bei Sandbox-Bedarf, mehreren Teams mit Roadmap-Planung oder hohem Automationsvolumen.

> Werte Stand Oktober 2026 – vor Angeboten auf atlassian.com/software/jira/pricing prüfen.

## 3. Projekttypen

| | Team-managed | Company-managed |
|---|---|---|
| Wer konfiguriert | Projekt-Admin selbst | Jira-Admin, über Schemes |
| Einstellungen teilbar | Nein, je Projekt | Ja, über mehrere Projekte |
| Geeignet für | Kleine, unabhängige Teams, schnelle Starts | Firmen mit Standards, Reporting über Projekte |
| Empfehlung im Beratungsprojekt | Nur für Experimente | **Standard für Kundenprojekte** |

## 4. Das Scheme-Modell (company-managed)

Jira-Konfiguration besteht aus wiederverwendbaren Bausteinen („Schemes“), die einem Projekt zugeordnet werden:

```
Projekt
 ├── Vorgangstypen-Schema      → welche Vorgangstypen (Aufgabe, Bug, Auftrag…)
 ├── Workflow-Schema           → welcher Workflow je Vorgangstyp
 ├── Vorgangstyp-Screen-Schema → welche Masken (Erstellen/Bearbeiten/Anzeigen)
 ├── Feldkonfigurations-Schema → Pflichtfelder, versteckte Felder
 ├── Berechtigungsschema       → wer darf was
 ├── Benachrichtigungsschema   → wer bekommt welche Mails
 ├── Sicherheitsstufen-Schema  → vertrauliche Vorgänge
 └── Prioritätsschema          → welche Prioritäten
```

**Goldene Regel:** So wenige Schemes wie möglich, so viele wie nötig. Ein Satz Schemes für ähnliche Projekte → einmal ändern, überall wirksam.

## 5. Hierarchie

Standard: **Epic → Vorgang (Aufgabe/Story/Bug) → Unteraufgabe**.
Premium/Enterprise: Weitere Ebenen darüber möglich (z. B. Initiative).

**Beispiel Maschinenbau-Auftrag:**
- Epic = Kundenauftrag (Maschine X für Kunde Y)
- Vorgänge = Gewerke/Arbeitspakete (Konstruktion, Elektrik, Montage, Inbetriebnahme)
- Unteraufgaben = konkrete Tätigkeiten

## 6. Felder – sparsam einsetzen

- Erst Standardfelder nutzen (Komponente, Label, Fälligkeitsdatum, Priorität, Lösung)
- Benutzerdefinierte Felder nur, wenn sie für Filter, Reports oder Automation gebraucht werden
- Felder **global wiederverwenden** statt pro Projekt neue anlegen („Kundennummer“ nur einmal)
- Feldtypen sinnvoll wählen: Auswahlliste statt Freitext, wenn ausgewertet werden soll
- Kontext (Projekt/Vorgangstyp) einschränken, damit Masken übersichtlich bleiben

## 7. Namenskonventionen

| Objekt | Konvention | Beispiel |
|---|---|---|
| Projektschlüssel | 2–5 Großbuchstaben, sprechend | `SVC`, `AUF`, `IT` |
| Workflow | `<Bereich> – <Prozess> – v<Nr>` | `Service – Reklamation – v1` |
| Schemes | `<Bereich> – <Typ>` | `Service – Berechtigungen` |
| Benutzerdefinierte Felder | Fachbegriff, keine Abkürzungen | `Seriennummer Maschine` |
| Gruppen | `jira-<bereich>-<rolle>` | `jira-service-agents` |
| Automationsregeln | `[Projekt] Auslöser → Aktion` | `[SVC] Erstellt → Zuweisen nach Komponente` |

## 8. Wichtige Begriffe (Spickzettel)

- **Status-Kategorien:** To Do (grau), In Progress (blau), Done (grün) – steuern Boards und Reports
- **Lösung (Resolution):** Muss beim Abschließen gesetzt werden, sonst gilt der Vorgang in Reports als offen
- **Komponente:** Teilbereich im Projekt, kann Standardbearbeiter haben
- **Version / Release:** Für Lieferstände (Software) oder Meilensteine
- **Board:** Scrum (Sprints) oder Kanban (Fluss) – basiert immer auf einem JQL-Filter
- **JQL:** Abfragesprache für Filter, Boards, Automation (siehe [Kapitel 10](10-reporting-jql.md))
