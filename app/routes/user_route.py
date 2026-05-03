from flask import Blueprint, request, jsonify
from app.services.user_service import create_user, get_all_users

user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Invalid data"}), 400

    user = create_user(data)

    return jsonify({
        "id": user.id,
        "status": "created"
    }), 201

@user_bp.route("/users", methods=["GET"])
def list_users():
    users = get_all_users()

    return jsonify([
        {
            "id": u.id,
            "username": u.username,
            "password_hash": u.password
        }
        for u in users
    ])