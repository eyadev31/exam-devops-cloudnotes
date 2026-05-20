from flask import Flask, jsonify
import os

app = Flask(__name__)

DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")

@app.route("/")
def home():
    return jsonify({
        "application": "CloudNotes",
        "message": "Bienvenue dans l'application CloudNotes",
        "database_host": DATABASE_HOST,
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "OK",
        "service": "cloudnotes"
    })

@app.route("/about")
def about():
    return jsonify({
        "application": "CloudNotes",
        "description": "Application web DevOps avec Flask, Docker et CI/CD"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
