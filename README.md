# mon-box — watchdog

Surveille le surveillant : vérifie toutes les 15 minutes que le Worker
[mon-box](https://mon-box.fpillet-mon-box.workers.dev) répond encore, et
prévient par mail sinon.

Sans ce filet, une panne de Cloudflare couperait silencieusement toutes les
alertes de coupure de courant.

| Secret | Rôle |
|---|---|
| `MONITOR_URL` | URL du Worker (sans slash final) |
| `HB_TOKEN` | jeton de l'endpoint `/` (query `token=`) |
| `SMTP_USER` / `SMTP_PASS` | compte Gmail + mot de passe d'application |
| `ALERT_EMAIL_TO` | destinataire |

Le job `keepalive` fait un commit hebdomadaire : GitHub désactive les workflows
planifiés d'un dépôt public sans activité depuis 60 jours.
