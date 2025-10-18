from flask import Flask, jsonify, request
import secrets
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
""" Api rest autenticacion y autorizacion"""


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = secrets.token_hex(32)
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    user = user.get(username)
    if user and check_password_hash(user["password"], password):
        return username

@app.route('/basic-protected')
def basic_protected():
    return jsonify(messege="Basic Auth: Access Granted"), 200

@app.route('/login', method=POST)
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    access_token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify(access_token=access_token), 200

@app.route('/jwt-protected')
@jwt_required()
def jwt_prtected():
    return jsonify(message="JWT Auth: Access Granted"), 200

@app.route('/admin-only')
@jwt_required()
def admin_only():
    if current_user["role"] != "admin":
        return jsonify()
    return jsonify(message="Admin Access: Granted"), 200

@jwt.unauthorized_loader
def 


if __name__ == '__main__':
    app.run()
