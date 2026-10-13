# 16 – Aktuelle Updates 2025–2026

Stand: **13.10.2026**. Atlassian ändert Jira Cloud laufend. Vor jedem Kundenprojekt kurz die Release-Notes und Preise prüfen.

## Überblick: Was ist neu und was heißt das für dich?

| Änderung | Seit | Bedeutung für Beratung |
|---|---|---|
| **Projekte → Spaces, Vorgänge → Work items** | Sept.–Dez. 2025 | Schulungsunterlagen und Begriffe anpassen |
| **Seat-Preiserhöhung Jira** | **13.10.2026** (heute) | Angebote mit neuen Preisen rechnen |
| **Automation wird nach Schritten abgerechnet** | Zählung seit 01.09.2026, **Abrechnung ab 03.12.2026** | Neues Beratungsfeld: Automation-Audit |
| **Rovo-Credits** (KI) mit Überschreitungskosten | 2026 | KI-Nutzung budgetieren |
| **JSM nur noch als „Service Collection“** | Neukunden seit 07.10.2025 | JSM + CSM + Assets + Rovo im Paket |
| **Saisonale Releases** (Frühling, Sommer) | Seit 2026 | Zweimal jährlich große Änderungen |
| **Connect-Apps Ende** | Q4 2026 | Kunden-Apps prüfen, ob sie auf Forge laufen |
| **Data Center Ende** | Abos laufen 28.03.2029 aus | Migrationen |
| **Neue Such-API** `/search/jql` | 2025 | Alte Skripte und Integrationen anpassen |

---

## 1. Neue Begriffe: Spaces und Work items
- Jira-**Projekte** heißen jetzt **Spaces** (wie in Confluence), **Vorgänge/Issues** heißen **Work items** bzw. „Arbeit“.
- Ausgerollt von September bis Dezember 2025, je nach Plan.
- **Gründe laut Atlassian:** „Projekt“ klingt nach zeitlich begrenzter Aufgabe, Jira-Container sind aber oft dauerhaft. Einheitlich mit Confluence. Und Atlassian hat ein eigenes Portfolio-Tool namens „Atlassian Projects“ gestartet.
- **Unverändert:** Workflows, Automationen, Rechte, Daten. JQL akzeptiert `project` vorerst weiter.
- **Kritik von Nutzern:** Verwirrend für Teams mit zeitlich begrenzten Aufträgen. Unklar, ob bei „Zugriff auf Space“ Jira oder Confluence gemeint ist. Teilweise noch gemischte Begriffe in der Oberfläche.
- **Für dich:** In Schulungen beide Begriffe nennen. Im Playbook steht oft noch „Projekt“ – gemeint ist dasselbe.

## 2. Preise (ab 13.10.2026)

| Jira-Plan | Alt (monatlich, pro Nutzer) | Neu |
|---|---|---|
| Free (bis 10 Nutzer) | 0 $ | 0 $ |
| Standard | 9,05 $ | **9,70 $** |
| Premium | 18,30 $ | **19,60 $** |
| Enterprise | auf Anfrage | auf Anfrage |

Bestehende Jahresabos behalten ihren Preis bis zur Verlängerung. Beispiel: 25 Standard-Nutzer zahlen rund 16 $ mehr pro Monat.

## 3. Automation wird nach Schritten abgerechnet

**Wichtigste Änderung für jeden Kunden mit Automationen!**

- Statt „Regelausführungen pro Monat“ zählt Atlassian jetzt **Schritte**: Jeder ausgeführte **Auslöser, jede Bedingung, Aktion, If/Else-Verzweigung und jeder Schleifendurchlauf** ist ein Schritt.
- **Auch ein Auslöser, der feuert, aber nichts findet, kostet einen Schritt.**
- Alle Produkte bilden einen **gemeinsamen Pool** in der Organisation.
- Zählung seit **01.09.2026**, Abrechnung ab **03.12.2026**.
- Überschreitung: **0,50 $ pro 1.000 Schritte**, standardmäßig **eingeschaltet**. Warnungen bei 80 % und 100 %.
- Ist Überschreitung ausgeschaltet, **stoppen Regeln bei 100 %** bis zum nächsten Abrechnungszeitraum.

**Inklusive Schritte (pro Nutzer und Monat, Free pro Abo):**

| Produkt | Free | Standard | Premium | Enterprise |
|---|---|---|---|---|
| Jira | 150 | 400 | 750 | 1.000 |
| Confluence | 50 | 100 | 250 | 500 |
| JSM / Service Collection | 1.250 | 3.000 | 6.500 | 9.500 |

**Was viele Schritte frisst:**
- Breiter Auslöser + enge Bedingung (z. B. „Vorgang aktualisiert“ und dann ein Feld prüfen)
- Stündliche geplante Regeln über breite JQL
- Teure Bedingungen vor billigen
- Schleifen über viele Vorgänge (z. B. alle Kinder eines Epics)
- Regeln, die sich gegenseitig auslösen
- Log-Aktionen im Normalfall

**So sparst du Schritte:**
1. **Enge Auslöser** nutzen (z. B. „Feldwert geändert“ statt „Vorgang aktualisiert“)
2. Geplante Regeln seltener laufen lassen, JQL enger fassen
3. **Billigste und selektivste Bedingung zuerst**
4. Regelketten **in eine Regel** zusammenlegen
5. Nur in Fehlerzweigen loggen
6. **Workflow-Post-Functions** statt Automation für Dinge, die an einem Übergang passieren (Feld setzen, zuweisen) – die werden nicht gezählt
7. Einfache Verzweigungen über Smart-Value-Bedingungen lösen (spart Schritte, ist aber schwerer nachzuvollziehen)
8. Bei viel Logik: Ereignis per einer Webanfrage an n8n oder eine Forge-App weitergeben

**Monatlich prüfen:** Verbrauch in der Atlassian-Administration unter Plattform-Nutzung, teuerste Regeln über die Leistungsübersicht finden. Audit-Log hält nur 90 Tage – Daten exportieren.

**Reaktion der Community:** Viele sehen es als versteckte Preiserhöhung. Andere begrüßen den Druck zu saubereren Regeln.

**→ Beratungsangebot „Automation-Audit vor dem 3. Dezember“:** Verbrauch analysieren, teure Regeln umbauen, Obergrenze setzen. Hoher Nutzen, schnell erledigt, gut verkaufbar.

## 4. Rovo (KI) und Credits
- Rovo-Agents arbeiten selbständig in Jira, Confluence und JSM: Vorgänge sortieren, zusammenfassen, Statusberichte schreiben. Agents können Vorgängen zugewiesen, erwähnt und in Workflows eingebaut werden.
- **Abrechnung in Credits:** Ein Chat oder ein Agent-Lauf kostet etwa 10 Credits, eine Tiefenrecherche etwa 100.
- **Inklusive pro Nutzer und Monat:** Standard 25, Premium 70, Enterprise 150. Free: keine.
- Überschreitung: 0,01 $ pro Credit, standardmäßig eingeschaltet – **Obergrenze setzen!**
- Rovo gibt es nur in der Cloud.
- **Empfehlung:** Pilot über 90 Tage mit festem Credit-Budget und klaren Erfolgszahlen.

## 5. Jira Service Management → Service Collection
- JSM wird für Neukunden (seit 07.10.2025) nur noch im Paket **Service Collection** verkauft: **JSM** (interne Services wie IT, HR, Facility) + **Customer Service Management (CSM)** für externe Kunden + **Assets** + **Rovo**.
- Bestandskunden wurden bis Mitte 2026 bei Verlängerung umgestellt. Preis pro Agent blieb laut Berichten gleich.
- **Free:** bis 3 Agents.
- **Assets-Grenzen** (Objekte): Standard 5.000, Premium 50.000, Enterprise 500.000. Darüber kostet jedes Objekt extra.
- **Für dich:** Maschinenbauer mit externen Kunden (Störungsmeldungen, Ersatzteile) können CSM nutzen – passt gut zu Service-Prozessen.

## 6. Saisonale Releases

### Frühling 2026
- **Agents in Jira:** Agents zuweisen, erwähnen, in Workflows einbauen
- **Rovo-Suche** direkt in Jira
- **Space-Dashboards** ersetzen den alten Reiter „Berichte“
- **„Für dich“-Seite:** persönliche Übersicht über zugewiesene Arbeit und Fristen
- **Gastzugang:** Externe kostenlos in einzelne Spaces einladen (höhere Pläne)
- **Geführte Einrichtung**
- **Eigene Space-Vorlagen** mit delegierten Rechten
- **Beta-Funktionen** zentral verwalten

**Kritik:** Neue Erstellen-Maske (Lösung: „Simple create“ aktivieren), Sprint-Reports schwerer zu finden, Funktionen teils nicht sichtbar trotz Ankündigung, einige Funktionen nur in höheren Plänen.

### Sommer 2026
- **Delivery Agent:** übernimmt Routinen wie Status-Checks, Standup-Zusammenfassungen, Updates an Stakeholder
- **Spaces per KI erstellen:** aus einer Beschreibung oder Dateien entsteht ein Space mit Workflows, Typen, Ansichten
- **Neue Listenansicht:** Liste und „Alle Arbeiten“ zusammengelegt, mit Hierarchie und Inline-Bearbeitung
- **Neue team-managed Boards:** schneller, mit Swimlanes und Unteraufgaben auf Karten
- **Kapazitätsansicht:** Wer ist ausgelastet, wer hat Luft?
- **Formelfelder:** Werte berechnen (z. B. Restbudget), Formel per KI aus Beschreibung
- **Schneller:** Vorgänge laden laut Atlassian rund 45 % schneller, Listen und Suche rund 48 %

## 7. Connect-Apps laufen aus
- Seit September 2025 müssen neue Marketplace-Apps mit **Forge** gebaut sein.
- Ab März 2026 können reine Connect-Apps nicht mehr aktualisiert werden.
- **Q4 2026:** Connect erreicht End of Support – nur noch kritische Sicherheitsfixes, Nutzung „auf eigenes Risiko“.
- **Für dich:** Bei jedem Kunden die installierten Apps prüfen. Apps ohne Forge-Version → Alternative suchen.

## 8. Data Center
- Seit 30.03.2026 keine Neukunden-Lizenzen mehr.
- Ab 30.03.2028 keine Erweiterungen mehr.
- **28.03.2029:** Data-Center-Abos laufen aus, Instanzen werden schreibgeschützt.
- Rovo und viele neue Funktionen gibt es nur in der Cloud.

## 9. API-Änderungen
- Alte Suche `/rest/api/3/search` ersetzt durch **`/search/jql`** mit Paging über `nextPageToken` (in den [Skripten](scripts/) schon umgesetzt).
- Begriffsänderungen (Spaces, Work items) betreffen laut Atlassian nicht die API-Felder – trotzdem nach jedem Release Integrationen testen.

---

## So bleibst du auf dem Laufenden
- **Atlassian Cloud Changes** (wöchentliche Liste aller Änderungen): confluence.atlassian.com/cloud/blog
- **Saisonale Release-Artikel** im Atlassian Blog und in der Community
- **Atlassian Community**, Bereich „Jira articles“
- **Release Tracks** (Premium/Enterprise): Änderungen gebündelt und verzögert erhalten – sinnvoll für Kunden mit Schulungsbedarf
- Eigene Gewohnheit: **jeden Monat 30 Minuten** Updates lesen und dieses Kapitel aktualisieren
