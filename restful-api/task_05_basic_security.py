from flask import Flask, abort, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "its_super_secret_from_Holberton"

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

print(generate_password_hash("password"))

@auth.verify_password
def verify_password(username, password):
    """Verifies user password"""
    # curl -u user1:password -X GET http://localhost:5000/basic-protected
    if username in users and \
        check_password_hash(users[username]["password"], password):
        return username

@app.route('/basic-protected')
@auth.login_required
def basic_auth():
    """Basic Authentication"""
    return "Basic Auth: Access Granted"

@app.route('/login', methods=["POST"])
def login():
    """login"""
    # -- Usage --
    # curl -X POST localhost:5000/login -H "Content-Type: application/json" -d '{"username": "user1", "password": "password"}'
    #curl -X POST localhost:5000/login -H "Content-Type: application/json" -d '{"username": "admin1", "password": "password"}'

    if request.get_json() is None:
        abort(400, "Not a JSON")

    data = request.get_json()

    for k in ["username", "password"]:
        if k not in data:
            abort(400, f"Missing attribute {k}.")

    username = data.get("username")
    password = data.get("password")

    if username not in users or not check_password_hash(users[username]["password"], password):
        return jsonify({"msg":'Invalid credentials'}), 401

    access_token = create_access_token(identity=data["username"])
    return jsonify({'access_token': access_token})

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    # curl -X GET http://localhost:5000/jwt-protected -H "Authorization: Bearer JWT_TOKEN"
    """Protected Route"""
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Only specific user have access"""
    actual_user = get_jwt_identity()

    if actual_user not in users or users[actual_user]["role"] != "admin":
        return jsonify({"error: Admin access required"}), 403

    return "Admin Access: Granted"
# Custom erro handle JWT  erros
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
    #app.run(host='localhost', port=5000, debug=True)
