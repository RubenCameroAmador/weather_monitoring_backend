from flask import Blueprint, request, jsonify
from app.services.auth_service import validate_user
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"]) 
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if validate_user(username, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"error": "Invalid credentials"}), 401