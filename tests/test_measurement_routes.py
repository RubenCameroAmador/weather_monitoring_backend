def test_ping(client):
    response = client.get("/api/ping")

    assert response.status_code == 200
    assert response.json["message"] == "pong"


def test_create_measurement(client):
    data = {
        "temperature": 25.0,
        "humidity": 60
    }

    response = client.post("/api/measurements", json=data)

    assert response.status_code == 201
    assert "id" in response.json


def test_invalid_measurement(client):
    response = client.post("/api/measurements", json={})

    assert response.status_code == 400

def test_get_latest_measurements(client):
    client.post("/api/measurements", json={
        "temperature": 25.5,
        "humidity": 60
    })

    client.post("/api/measurements", json={
        "temperature": 26.0,
        "humidity": 65
    })

    response = client.get("/api/measurements/latest")

    assert response.status_code == 200

    data = response.get_json()

    assert isinstance(data, list)
    assert len(data) > 0

    first = data[0]
    assert "temperature" in first
    assert "humidity" in first
    assert "created_at" in first
