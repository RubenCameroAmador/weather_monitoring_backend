from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.measurement_service import (
    create_measurement,
    get_latest_measurements
)

measurement_bp = Blueprint("measurement", __name__)


@measurement_bp.route("/measurements", methods=["POST"])
@jwt_required()
def add_measurement():
    data = request.get_json()
    current_user = get_jwt_identity()


    if not data or "temperature" not in data or "humidity" not in data:
        return jsonify({"error": "Invalid data"}), 400

    measurement = create_measurement(data)

    return jsonify({
        "id": measurement.id,
        "status": "created"
    }), 201


@measurement_bp.route("/measurements/latest", methods=["GET"])
@jwt_required()
def latest_measurements():
    current_user = get_jwt_identity()

    measurements = get_latest_measurements()

    return jsonify([
        {
            "temperature": m.temperature,
            "humidity": m.humidity,
            "created_at": m.created_at.isoformat()
        }
        for m in measurements
    ])

@measurement_bp.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"}), 200