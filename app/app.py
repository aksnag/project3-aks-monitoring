from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = Flask(__name__)

# Create a request counter metric
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests received"
)

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    time.sleep(random.uniform(0.1, 0.5))  # simulate work
    return "Project 3 - Monitoring Enabled Flask App 🚀"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
