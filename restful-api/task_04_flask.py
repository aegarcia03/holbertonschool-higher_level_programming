#!/usr/bin/python3
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    """Returns a string"""
    return "Welcome to the Flask API!"

@app.route("/data")
def get_users():
    """Returns a list of all the usernames stored in the API"""
    if not users:
        return jsonify([]), 200
    return jsonify(list(users.keys())), 200

@app.route("/status")
def status():
    """Prints ok"""
    return "OK"

@app.route("/users/<username>")
def find_user(username):
    """Dynamic Route
    Returns details about specific username"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    user_name = users[username]
    user_name["username"] = username
    return jsonify(user_name)

@app.route("/add_user", methods=['POST'])
def add_user():
    """Adds the user to the users dictionary"""
    if request.get_json() is None:
        abort(400, "Not a JSON")

    info_user = request.get_json()
    if "username" not in info_user:
        return jsonify({"error": "Username is required"}), 400

    username = info_user['username']
    users[username] = {
        "name": info_user.get("name"),
        "age": info_user.get("age"),
        "city": info_user.get("city")
    }

    output = {
        "username": username,
        "name": users[username]["name"],
        "age": users[username]["age"],
        "city": users[username]["city"]
    }

    return jsonify({"message": "User added", "user" : output}), 201

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
