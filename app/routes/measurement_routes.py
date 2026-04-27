from flask import Blueprint, request, jsonify
from app.services.measurement_service import (
    create_measurement,
    get_latest_measurements
)

measurement_bp = Blueprint("measurement", __name__)


@measurement_bp.route("/measurements", methods=["POST"])
def add_measurement():
    data = request.get_json()

    if not data or "temperature" not in data or "humidity" not in data:
        return jsonify({"error": "Invalid data"}), 400

    measurement = create_measurement(data)

    return jsonify({
        "id": measurement.id,
        "status": "created"
    }), 201


@measurement_bp.route("/measurements/latest", methods=["GET"])
def latest_measurements():
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