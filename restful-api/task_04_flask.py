#!/usr/bin/python3
"""Api Flask"""


from flask import Flask, jsonify, request


app = Flask(__name__)
#diccionario inicial de usuarios
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/status")
def status():
    return "OK"

@app.route("/data/<usernames>")
def get_usernames():
    #devuelve solo username
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"})

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    #checkear que username eeste en json
    if not data or "username" not in data:
       return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
