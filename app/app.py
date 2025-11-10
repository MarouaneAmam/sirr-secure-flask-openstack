from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "service": "sirr-secure-flask-openstack",
        "version": "0.1.0",
        "env": os.getenv("APP_ENV", "dev")
    })

@app.route("/healthz")
def healthz():
    return jsonify({"status": "ok"}), 200

@app.route("/api/v1/ping")
def ping():
    return jsonify({"ping": "pong"}), 200
