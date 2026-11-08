"""Alerte par mail quand le Worker mon-box ne repond plus.

Utilise le meme compte Gmail que le Worker (mot de passe d'application),
pour rester coherent avec les autres alertes.
"""
import os
import smtplib
import ssl
from email.message import EmailMessage

user = os.environ["SMTP_USER"]
password = os.environ["SMTP_PASS"]
to = os.environ["ALERT_EMAIL_TO"]
url = os.environ.get("MONITOR_URL", "")

msg = EmailMessage()
msg["Subject"] = "mon-box : la surveillance ne repond plus"
msg["From"] = user
msg["To"] = to
msg.set_content(
    "Le Worker mon-box ne repond plus (2 tentatives a 30 s d'intervalle).\n\n"
    f"URL surveillee : {url}\n\n"
    "Consequences : plus aucune alerte de coupure de courant ne peut partir.\n"
    "A verifier :\n"
    "  1. le Worker et la base D1 sur https://dash.cloudflare.com\n"
    "  2. l'etat de Cloudflare : https://www.cloudflarestatus.com\n"
    "  3. que les secrets (HB_TOKEN, SMTP_*) sont toujours en place\n"
)

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as smtp:
    smtp.login(user, password)
    smtp.send_message(msg)

print(f"alerte envoyee a {to}")
