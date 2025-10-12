#!/usr/bin/python3
"""Flask API"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Diccionario de usuarios vacío
users = {}

# Ruta principal
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Ruta /status
@app.route("/status")
def status():
    return "OK"

# Ruta /data que devuelve todos los usernames
@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))

# Ruta dinámica para cada usuario
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Ruta para agregar usuarios
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    # Validación mínima según el enunciado
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201

# Arrancar el servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
