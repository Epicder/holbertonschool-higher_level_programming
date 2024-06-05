#!/usr/bin/python3

from flask import Flask, jsonify, request


app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route("/")
def home():
    print("Welcome to the Flask API!")

@app.route("/data", methods=['GET'])
def return_json():
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route("/status", methods=['GET'])
def status():
    return "OK", 200

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json()
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    users[username] = {
        "name": new_user.get("name"),
        "age": new_user.get("age"),
        "city": new_user.get("city")
    }
    return jsonify({"message": "User added successfully", "user": users[username]}), 201             

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
