import threading
import time
import random
import signal
import sys
from logger import log_attempt, stop_logger
from config import SIMULATE_INTERVAL_SEC

_stop = threading.Event()
_worker = None

FAKE_IPS = [
    "177.22.19.88", "185.93.11.5", "93.184.216.34",
    "45.55.11.101", "200.147.35.60"
]

USERNAMES = ["root", "admin", "postgres", "test", "user"]
PASSWORDS = ["123456", "admin", "toor", "password", "letmein", "qwerty"]

def _simulate():
    print("[honeypot] Rodando. Pressione CTRL+C para parar.")
    while not _stop.is_set():
        ip = random.choice(FAKE_IPS)
        user = random.choice(USERNAMES)
        pw = random.choice(PASSWORDS)
        log_attempt(ip, user, pw, {"source": "simulator"})
        time.sleep(SIMULATE_INTERVAL_SEC)

def start():
    global _worker
    if _worker and _worker.is_alive():
        print("[honeypot] já está ativo.")
        return
    _stop.clear()
    _worker = threading.Thread(target=_simulate, daemon=True)
    _worker.start()
    print("[honeypot] iniciado.")

def stop():
    _stop.set()
    if _worker:
        _worker.join(timeout=2)
    stop_logger()
    print("[honeypot] parado.")

def status():
    return "running" if (_worker and _worker.is_alive()) else "stopped"

def signal_handler(sig, frame):
    print("\nEncerrando...")
    stop()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    print("Comandos: start | stop | status | exit")
    while True:
        cmd = input("> ").strip().lower()
        if cmd == "start":
            start()
        elif cmd == "stop":
            stop()
        elif cmd == "status":
            print("Status:", status())
        elif cmd in ["exit", "quit"]:
            stop()
            break
        else:
            print("Comando inválido.")
