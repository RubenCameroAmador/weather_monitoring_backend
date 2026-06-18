from app.extensions import socketio


def test_connect_without_token_allowed_by_test_client(app):
    client = socketio.test_client(app)
    try:
        client.disconnect()
    except RuntimeError:
        pass


def test_connect_with_valid_token(app):
    with app.app_context():
        from flask_jwt_extended import create_access_token
        token = create_access_token(identity="test_user")
    client = socketio.test_client(app, auth={"token": token})
    assert client.is_connected()
    client.disconnect()


def test_connect_with_query_string_token(app):
    with app.app_context():
        from flask_jwt_extended import create_access_token
        token = create_access_token(identity="test_user")
    client = socketio.test_client(app, query_string=f"token={token}")
    assert client.is_connected()
    client.disconnect()


def test_new_measurement_broadcast(app, auth_headers):
    with app.app_context():
        from flask_jwt_extended import create_access_token
        token = create_access_token(identity="test_user")

    ws_client = socketio.test_client(app, auth={"token": token})
    assert ws_client.is_connected()

    with app.test_client() as http_client:
        response = http_client.post(
            "/api/measurements",
            json={"temperature": 25.5, "humidity": 60.0},
            headers=auth_headers,
        )
        assert response.status_code == 201

    received = ws_client.get_received()
    new_meas = [e for e in received if e["name"] == "new_measurement"]
    assert len(new_meas) == 1
    data = new_meas[0]["args"][0]
    assert data["temperature"] == 25.5
    assert data["humidity"] == 60.0
    assert "id" in data
    assert "created_at" in data

    ws_client.disconnect()
