from flask import Flask, jsonify
import socket
from datetime import datetime

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "task": "Learn Docker",
        "status": "completed"
    },
    {
        "id": 2,
        "task": "Learn Jenkins",
        "status": "in-progress"
    }
]

@app.route("/")
def home():
    return jsonify({
        "message": "Task API is running",
        "hostname": socket.gethostname(),
        "timestamp": str(datetime.now())
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })
##########
@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
