import os
import json
import threading
import queue
import datetime
from config import LOG_TXT, LOG_JSONL

os.makedirs(os.path.dirname(LOG_TXT), exist_ok=True)

_write_queue = queue.Queue()
_stop_event = threading.Event()

def _worker():
    while not _stop_event.is_set() or not _write_queue.empty():
        try:
            item = _write_queue.get(timeout=0.5)
        except:
            continue

        try:
            with open(LOG_TXT, "a", encoding="utf-8") as f:
                f.write(item["txt"] + "\n")

            with open(LOG_JSONL, "a", encoding="utf-8") as j:
                j.write(json.dumps(item["json"], ensure_ascii=False) + "\n")

        except Exception as e:
            print("Erro ao registrar log:", e)

        finally:
            _write_queue.task_done()

_thread = threading.Thread(target=_worker, daemon=True)
_thread.start()

def log_attempt(ip, username, password, meta=None):
    now = datetime.datetime.utcnow().isoformat() + "Z"
    txt = f"{now} | IP:{ip} | USER:{username} | PASS:{password}"

    payload = {
        "timestamp": now,
        "ip": ip,
        "username": username,
        "password": password,
    }
    if meta:
        payload["meta"] = meta

    _write_queue.put({"txt": txt, "json": payload})

def stop_logger():
    _stop_event.set()
    _thread.join(timeout=3)
