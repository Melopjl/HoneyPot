from flask import Flask, render_template, jsonify, Response
from stats import get_stats
from config import LOG_TXT, FLASK_HOST, FLASK_PORT
import csv
import io

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/logs")
def logs():
    try:
        with open(LOG_TXT, "r", encoding="utf-8", errors="ignore") as f:
            return jsonify({"logs": f.read()})
    except:
        return jsonify({"logs": ""})

@app.route("/stats")
def stats():
    return jsonify(get_stats())

@app.route("/export.csv")
def export_csv():
    data = get_stats()["last_entries"]
    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(["timestamp", "ip", "username", "password"])
    for d in data:
        writer.writerow([d["timestamp"], d["ip"], d["username"], d["password"]])

    return Response(output.getvalue(),
                    mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=honeypot.csv"})

if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT)
