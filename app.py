from flask import Flask
import os
import platform

app = Flask(__name__)

LOG_FILE = "/var/log/syslog"

def read_logs():
    logs = []
    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()[-25:]
            for line in lines:
                if "error" in line.lower() or "fail" in line.lower():
                    logs.append(line.strip())
    except Exception as e:
        logs.append(str(e))
    return logs

@app.route("/")
def home():
    logs = read_logs()

    html = """
    <html>
    <head>
        <title>Log Monitor Dashboard</title>
        <style>
            body {
                background: #0f172a;
                font-family: Arial;
                color: white;
                margin: 0;
                padding: 0;
            }
            .header {
                background: #2563eb;
                padding: 20px;
                text-align: center;
                font-size: 28px;
                font-weight: bold;
            }
            .container {
                padding: 20px;
            }
            .card {
                background: #1e293b;
                padding: 15px;
                margin: 10px 0;
                border-radius: 10px;
                box-shadow: 0px 0px 10px #000;
            }
            .error {
                color: #f87171;
                font-size: 14px;
            }
            .ok {
                color: #4ade80;
            }
        </style>
    </head>
    <body>

    <div class="header">🔥 Log Monitoring Dashboard</div>

    <div class="container">

        <div class="card">
            <h2>System Info</h2>
            <p>OS: """ + platform.system() + """</p>
            <p>User: """ + str(os.getenv("USER")) + """</p>
            <p>Directory: """ + os.getcwd() + """</p>
        </div>

        <div class="card">
            <h2>🚨 Error Logs</h2>
    """

    if logs:
        for log in logs:
            html += f"<p class='error'>{log}</p>"
    else:
        html += "<p class='ok'>No errors found 🎉</p>"

    html += """
        </div>

    </div>

    </body>
    </html>
    """

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
