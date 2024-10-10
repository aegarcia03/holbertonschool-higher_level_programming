from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
    }

@app.route("/")
def home():
    """Returns a string"""
    return "Welcome to the Flask API"

@app.route("/data")
def get_users():
    """Returns a list of all the usernames stored in the API"""
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """Pritns ok"""
    return "OK"

@app.route("/users/<username>")
def find_user(username):
    """Dynamic Route
    Returns details about specific username"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    else:
        return jsonify(users[username])

@app.route("/add_user", methods=['POST'])
def add_user():
    """Adds the user to the users dictionary"""
    info_user = request.get_json()

    if "username" not in info_user:
        return jsonify({"error": "Username is required"}), 400

    username = info_user['username']
    users[username] = info_user

    return jsonify({"message": "User added", "user" : info_user}), 201

if __name__ == "__main__":
    app.run()
