# 07 – Integrationen

## Entscheidungsbaum: Wie integriere ich?

```
Gibt es eine fertige App/Integration (Marketplace, offizielle Integration)?
 ├─ Ja → nutzen (schnell, gewartet). Kosten & Datenschutz prüfen.
 └─ Nein → Reicht Jira Automation (Webanfrage / eingehender Webhook)?
      ├─ Ja → Automation (kein eigener Server nötig)
      └─ Nein → Mehrere Systeme / Logik / Daten umbauen?
           ├─ Ja, ohne viel Code → n8n / Make / Power Automate
           └─ Ja, komplex/dauerhaft → eigenes Skript/Service (REST API) oder Forge-App
```

---

## 1. REST API (Jira Cloud, v3)

**Basis-URL:** `https://<firma>.atlassian.net/rest/api/3/`

**Anmeldung:**
| Methode | Wann |
|---|---|
| E-Mail + API-Token (Basic Auth) | Eigene Skripte, interne Integrationen. Token: id.atlassian.com → Sicherheit → API-Token |
| OAuth 2.0 (3LO) | Apps, die im Namen verschiedener Nutzer handeln |
| Forge-App | Code läuft bei Atlassian, Auth automatisch |

**Wichtige Endpunkte:**

| Zweck | Methode & Pfad |
|---|---|
| Vorgang lesen | `GET /issue/{key}` |
| Vorgang erstellen | `POST /issue` |
| Vorgang ändern | `PUT /issue/{key}` |
| Übergänge abfragen | `GET /issue/{key}/transitions` |
| Übergang ausführen | `POST /issue/{key}/transitions` |
| Kommentar | `POST /issue/{key}/comment` |
| Suche (JQL) | `GET` oder `POST /search/jql` (Paging über `nextPageToken`) |
| Alle Felder (IDs!) | `GET /field` |
| Projekte | `GET /project/search` |
| Nutzer suchen | `GET /user/search?query=...` |
| Metadaten zum Erstellen | `GET /issue/createmeta/{projectKey}/issuetypes` |

**Wichtig:**
- Beschreibungen/Kommentare in v3 sind im **Atlassian Document Format (ADF)** (JSON), nicht Klartext. Beispiel in [scripts/jira_client.py](scripts/jira_client.py)
- Nutzer werden über **accountId** angesprochen, nicht über Name/Mail
- **Rate Limits** beachten: Bei HTTP 429 den `Retry-After`-Header abwarten
- Die alte Suche `/rest/api/3/search` wurde durch `/search/jql` ersetzt – alte Skripte prüfen

**JSM-API:** `https://<firma>.atlassian.net/rest/servicedeskapi/` (Request Types, Kunden, Organisationen, Queues, SLAs)

**Bibliotheken:**
- Python: `atlassian-python-api` oder `jira` (pycontribs)
- Go: `andygrunwald/go-jira`
- Kommandozeile: `ankitpokhrel/jira-cli`

## 2. Webhooks

- **Ausgehend:** Jira ruft bei Ereignissen (Vorgang erstellt/geändert, Kommentar…) eine URL auf. Einrichtung: Einstellungen → System → Webhooks, mit JQL-Filter
- **Alternativ:** Automation-Aktion „Webanfrage senden“ – flexibler (eigener Body)
- **Eingehend:** Automation-Auslöser „Eingehender Webhook“ – externes System ruft Jira-URL auf und startet eine Regel
- Empfänger-Beispiel: [scripts/webhook_receiver.py](scripts/webhook_receiver.py)

## 3. Forge (eigene Jira-Apps)

- Atlassians Plattform für Apps, die **in Jira laufen** (eigene Panels, Felder, Workflow-Validatoren, geplante Jobs)
- JavaScript/TypeScript, Hosting bei Atlassian, CLI: `npm install -g @forge/cli`
- Connect (alte App-Technik) wird abgelöst → neue Apps immer mit Forge
- Einstieg: Forge-Doku auf developer.atlassian.com, Beispiele: `andrei-pisklenov/awesome-forge`, `kannonboy/forge-scheduler`
- Geschäftsmodell: Eigene App im Atlassian Marketplace verkaufen

## 4. No-/Low-Code: n8n, Make, Power Automate

| Tool | Stärke | Hinweis |
|---|---|---|
| **n8n** | Selbst hostbar (DSGVO), sehr flexibel, Jira-Nodes vorhanden | Lizenz: für Kunden einrichten ok, n8n selbst nicht als eigenen SaaS weiterverkaufen |
| **Make** | Einfach, viele Apps | Cloud, EU-Region wählbar |
| **Power Automate** | Ideal bei Microsoft-365-Kunden | Jira-Connector vorhanden |

**Typische Flows:**
- Formular (Website/Typeform) → Jira-Vorgang
- Jira-Vorgang erledigt → Rechnung/Lieferschein im ERP anstoßen
- E-Mail mit Anhang → Vorgang + Anhang in SharePoint ablegen
- CRM-Deal gewonnen → Projekt-Epic mit Standard-Aufgaben in Jira

## 5. Kommunikation

- **Microsoft Teams:** offizielle App „Jira Cloud for Microsoft Teams“ (Benachrichtigungen, Vorgänge erstellen)
- **Slack:** offizielle Jira-App + JSM-Integration (Anfragen direkt aus Slack)
- **E-Mail:** JSM-E-Mail-Kanal; für Jira Software: „Vorgang per E-Mail erstellen“ oder Automation mit Mail-Auslöser

## 6. Entwicklung

- **GitHub / GitLab / Bitbucket:** offizielle Integrationen verknüpfen Commits, Branches, PRs mit Vorgängen über den **Vorgangsschlüssel** im Commit/Branch-Namen (`SVC-123-fix-login`)
- **CI/CD:** Deployments in Jira sichtbar (GitHub Actions, GitLab CI, Bitbucket Pipelines)

## 7. Login & Nutzerverwaltung

- **SSO / SAML:** Microsoft Entra ID, Google, Okta über Atlassian Guard (in Enterprise enthalten, sonst Zusatzabo – prüfen)
- **Nutzer-Provisionierung (SCIM):** Nutzer automatisch aus Entra ID anlegen/deaktivieren

## 8. KI-Integration

| Weg | Was |
|---|---|
| **Atlassian Rovo** | KI direkt in Jira/Confluence (Suche, Agents, Zusammenfassungen) |
| **Atlassian Remote MCP Server** (`atlassian/atlassian-mcp-server`) | Offizieller Weg, um Claude, ChatGPT & Co. mit Jira, Confluence, JSM zu verbinden (OAuth) |
| **mcp-atlassian** (`sooperset/mcp-atlassian`) | Beliebter Community-Server, selbst hostbar, Cloud + Data Center |
| **atlassian-dc-mcp** (`b1ff/atlassian-dc-mcp`) | Für Data-Center-Instanzen |

Anwendungsfälle: Tickets aus Beschreibungen erstellen lassen, Backlog zusammenfassen, Wochenberichte erzeugen, Wissensartikel aus gelösten Tickets.
**Datenschutz:** Vorher klären, welche Daten an welchen KI-Anbieter gehen (AVV, Datenresidenz).

## 9. Konfiguration als Code

- **Terraform-Provider** (`fourplusone/terraform-provider-jira`, Atlassian-Operations-Provider für JSM-Operations) – für Firmen mit Infrastructure-as-Code
- Für KMU meist zu viel – besser: Konfiguration im Konzept dokumentieren + Sandbox (Premium)

## Integrations-Checkliste
- [ ] Ziel und Datenfluss gezeichnet (Was geht wohin, wann, wer löst aus?)
- [ ] Eigener technischer Nutzer / Service-Account mit minimalen Rechten
- [ ] API-Token sicher gespeichert (nie im Code, nie in GitHub!)
- [ ] Fehlerfall geklärt: Wiederholung, Benachrichtigung, Protokoll
- [ ] Rate Limits berücksichtigt
- [ ] Datenschutz geprüft (personenbezogene Daten, AVV)
- [ ] Getestet mit echten Beispielen
- [ ] Dokumentiert im Betriebshandbuch
