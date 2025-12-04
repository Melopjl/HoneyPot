import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_TXT = os.path.join(BASE_DIR, "logs", "attempts.log")
LOG_JSONL = os.path.join(BASE_DIR, "logs", "attempts.jsonl")

SIMULATE_INTERVAL_SEC = 2.0  

FLASK_HOST = "127.0.0.1"
FLASK_PORT = 5000
