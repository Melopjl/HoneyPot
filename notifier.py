import os
import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, DISCORD_WEBHOOK

def send_telegram(text):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        return False
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try:
        r = requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": text})
        return r.ok
    except Exception:
        return False

def send_discord(text):
    if not DISCORD_WEBHOOK:
        return False
    try:
        r = requests.post(DISCORD_WEBHOOK, json={"content": text})
        return r.ok
    except Exception:
        return False

def notify_all(text):
    try:
        send_telegram(text)
        send_discord(text)
    except Exception:
        pass
