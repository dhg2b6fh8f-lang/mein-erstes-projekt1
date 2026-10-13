"""Minimaler Empfänger für Jira-Webhooks bzw. Automation-„Webanfrage senden“.

- Prüft ein gemeinsames Geheimnis im Header X-Webhook-Secret
- Reagiert auf neu erstellte Vorgänge (hier: nur Ausgabe – hier eigene Logik einbauen,
  z. B. ERP-Auftrag anlegen, Teams-Nachricht senden, Kommentar zurückschreiben)

Start lokal:   WEBHOOK_SECRET=geheim python webhook_receiver.py
Öffentlich erreichbar machen (zum Testen): z. B. mit einem Tunnel-Dienst; produktiv auf einem Server mit HTTPS.

In Jira Automation: Aktion „Webanfrage senden“
    URL:     https://dein-server/jira
    Header:  X-Webhook-Secret: geheim
    Body:    Benutzerdefiniert, z. B.
             {"key": "{{issue.key}}", "summary": "{{issue.summary}}", "event": "created"}
"""
import hmac
import os

from flask import Flask, abort, jsonify, request

app = Flask(__name__)
SECRET = os.environ.get("WEBHOOK_SECRET", "")


@app.post("/jira")
def jira_webhook():
    sent = request.headers.get("X-Webhook-Secret", "")
    if not SECRET or not hmac.compare_digest(sent, SECRET):
        abort(401)

    data = request.get_json(silent=True) or {}

    # Format 1: eigener Body aus Automation
    key = data.get("key")
    summary = data.get("summary")
    event = data.get("event")

    # Format 2: Standard-Jira-Webhook (System → Webhooks)
    if not key and "issue" in data:
        key = data["issue"].get("key")
        summary = data["issue"].get("fields", {}).get("summary")
        event = data.get("webhookEvent")

    print(f"Ereignis={event} Vorgang={key} Zusammenfassung={summary}")

    # TODO: Eigene Logik hier, z. B.:
    # from jira_client import JiraClient
    # JiraClient().add_comment(key, "Auftrag im ERP angelegt.")

    return jsonify({"ok": True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
