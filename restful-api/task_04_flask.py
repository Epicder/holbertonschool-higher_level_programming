#!/usr/bin/python3

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route("/", methods=['GET'])
def home():
    return "Welcome to the User API", 200

@app.route("/data", methods=['GET'])
def get_usernames():
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route("/users/<username>", methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        abort(404, description="User not found")

@app.route("/add_user", methods=['POST'])
def add_user():
    new_user = request.get_json()
    username = new_user.get("username")
    
    if not username:
        abort(400, description="Username is required")
    
    if username in users:
        abort(400, description="User already exists")
    
    users[username] = {
        "name": new_user.get("name"),
        "age": new_user.get("age"),
        "city": new_user.get("city")
    }
    
    return jsonify({"message": "User added successfully", "user": users[username]}), 201

@app.route("/status", methods=['GET'])
def status():
    return jsonify({"status": "OK"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
