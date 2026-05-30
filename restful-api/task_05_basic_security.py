#!/usr/bin/env python3
"""
API Security and Authentication Techniques
Implementation of Basic Auth, JWT Auth, and Role-Based Access Control.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, get_jwt_identity,
    jwt_required
)

app = Flask(__name__)

# Security keys configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key-here'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Mock Data: Users stored in memory
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# ---------------------------------------------------------
# BASIC AUTHENTICATION
# ---------------------------------------------------------

@auth.verify_password
def verify_password(username, password):
    """Verifies the username and hashed password."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

@auth.error_handler
def auth_error():
    """Returns 401 for unauthorized Basic Auth requests."""
    return jsonify({"error": "Unauthorized access"}), 401

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Protected route using Basic HTTP Authentication."""
    return "Basic Auth: Access Granted"

# ---------------------------------------------------------
# JWT AUTHENTICATION & ROLE-BASED ACCESS CONTROL
# ---------------------------------------------------------

@app.route('/login', methods=['POST'])
def login():
    """Authenticates a user and returns a JWT token."""
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = users.get(username)
    
    # Check if user exists and password is correct
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Embed user information (username and role) into the token payload
    access_token = create_access_token(
        identity={"username": username, "role": user["role"]}
    )
    return jsonify({"access_token": access_token})

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Protected route using JWT."""
    return "JWT Auth: Access Granted"

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Protected route requiring Admin role."""
    current_user = get_jwt_identity()
    
    # Check if the user's role matches 'admin'
    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
        
    return "Admin Access: Granted"

# ---------------------------------------------------------
# CUSTOM JWT ERROR HANDLERS (Enforcing 401 status)
# ---------------------------------------------------------

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

# ---------------------------------------------------------
# EXECUTION
# ---------------------------------------------------------

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
