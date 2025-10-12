#!/usr/bin/python3
"""Flask API"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Diccionario de usuarios vacío al inicio
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/status")
def status():
    return "OK"

@app.route("/data")
def get_all_users():
    # Devuelve solo la lista de usernames
    return jsonify(list(users.keys())), 200

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    # Validación obligatoria
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # Validación duplicados EXACTA para pasar el test
    if username in users:
        return app.response_class(
            response='{"error": "User already exists"}',
            status=400,
            mimetype='application/json'
        )

    # Guardar usuario con todos los campos requeridos
    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
