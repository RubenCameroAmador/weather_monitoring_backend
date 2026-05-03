def test_create_user(client):
    data = {
        "username": "testuser",
        "password": "testpassword"
    }

    response = client.post("/api/users", json=data)

    assert response.status_code == 201
    assert "id" in response.json

def test_invalid_user(client):
    response = client.post("/api/users", json={})

    assert response.status_code == 400

def test_list_users(client):
    client.post("/api/users", json={
        "username": "user1",
        "password": "pass1"
    })  

    response = client.get("/api/users")

    assert response.status_code == 200
    assert len(response.json) == 1