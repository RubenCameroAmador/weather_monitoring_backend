from flask import request
import jwt
from flask_jwt_extended import decode_token
from flask_jwt_extended.exceptions import JWTExtendedException
from app.extensions import socketio
from app.services.measurement_service import get_latest_measurements


@socketio.on("connect")
def handle_connect(auth):
    token = None
    if auth and isinstance(auth, dict):
        token = auth.get("token")
    if not token:
        token = request.args.get("token")
    if not token:
        return False
    try:
        decode_token(token)
    except (JWTExtendedException, jwt.ExpiredSignatureError):
        return False


@socketio.on("disconnect")
def handle_disconnect():
    pass


@socketio.on("get_latest")
def handle_get_latest():
    measurements = get_latest_measurements()
    socketio.emit("latest_measurements", [
        {
            "temperature": m.temperature,
            "humidity": m.humidity,
            "created_at": m.created_at.isoformat()
        }
        for m in measurements
    ])
