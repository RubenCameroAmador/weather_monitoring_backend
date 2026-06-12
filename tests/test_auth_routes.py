def test_login_returns_access_and_refresh_tokens(client):
    client.post("/api/users", json={
        "username": "testuser",
        "password": "testpass"
    })

    response = client.post("/api/login", json={
        "username": "testuser",
        "password": "testpass"
    })

    assert response.status_code == 200
    assert "access_token" in response.json
    assert "refresh_token" in response.json


def test_login_invalid_credentials(client):
    response = client.post("/api/login", json={
        "username": "nonexistent",
        "password": "wrong"
    })

    assert response.status_code == 401
    assert response.json["error"] == "Invalid credentials"


def test_refresh_returns_new_access_token(client, app):
    client.post("/api/users", json={
        "username": "testuser",
        "password": "testpass"
    })

    login_resp = client.post("/api/login", json={
        "username": "testuser",
        "password": "testpass"
    })
    refresh_token = login_resp.json["refresh_token"]

    response = client.post(
        "/api/refresh",
        headers={"Authorization": f"Bearer {refresh_token}"}
    )

    assert response.status_code == 200
    assert "access_token" in response.json
    assert response.json["access_token"] != login_resp.json["access_token"]


def test_refresh_fails_with_access_token(client):
    client.post("/api/users", json={
        "username": "testuser",
        "password": "testpass"
    })

    login_resp = client.post("/api/login", json={
        "username": "testuser",
        "password": "testpass"
    })
    access_token = login_resp.json["access_token"]

    response = client.post(
        "/api/refresh",
        headers={"Authorization": f"Bearer {access_token}"}
    )

    assert response.status_code == 422


def test_refresh_fails_without_token(client):
    response = client.post("/api/refresh")

    assert response.status_code == 401
