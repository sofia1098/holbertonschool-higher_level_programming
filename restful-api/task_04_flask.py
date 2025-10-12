#!/usr/bin/python3
"""Flask API"""


from flask import Flask, jsonify, request

app = Flask(__name__)

# Diccionario de usuarios
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/status")
def status():
    return "OK"

@app.route("/data")
def get_all_users():
    #return la lista de todos los usuarios
    return jsonify(list(users.values())), 200

@app.route("/users/<username>")
def get_user(username):
    #return información de un usuario
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    #Agrega nuevo usuario
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = data

    return jsonify({
        "message": "User added successfully",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
