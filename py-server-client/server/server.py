from flask import Flask, request, jsonify
import os

app = Flask(__name__)
API_TOKEN = os.environ.get("API_TOKEN", "super-secret-token")

@app.route("/ping", methods=["GET"])
def ping():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Unauthorized"}), 401

    token = auth_header.split(" ")[1]
    if token != API_TOKEN:
        return jsonify({"error": "Invalid token"}), 403

    return jsonify({"message": "pong"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
