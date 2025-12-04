import json
from collections import Counter
from config import LOG_JSONL

def get_stats():
    try:
        with open(LOG_JSONL, "r", encoding="utf-8") as f:
            lines = [json.loads(l) for l in f if l.strip()]
    except FileNotFoundError:
        lines = []

    ips = [l["ip"] for l in lines]
    users = [l["username"] for l in lines]

    return {
        "total_attempts": len(lines),
        "top_ips": Counter(ips).most_common(10),
        "top_usernames": Counter(users).most_common(10),
        "last_entries": lines[-50:]
    }
