from flask import Flask
import os

app = Flask(__name__)

TASKS = []
MEMORY = {
    "system": "Dean'z Elite OS",
    "mode": "foundation",
    "notes": [
        "OpenShift deployment lifecycle verified",
        "GitHub source ownership verified",
        "Health, status, and task endpoints active"
    ]
}

@app.route('/')
def hello():
    return "Dean'z Elite OS Foundation Online"

@app.route('/health')
def health():
    return {"status": "online"}

@app.route('/status')
def status():
    return {
        "app": "task-planner-foundation",
        "system": "Dean'z Elite OS Foundation",
        "status": "running",
        "phase": "foundation-api"
    }

@app.route('/tasks')
def tasks():
    return {
        "tasks": TASKS,
        "count": len(TASKS)
    }

@app.route('/memory')
def memory():
    return MEMORY

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port, host='0.0.0.0')
