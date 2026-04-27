from app.services.measurement_service import create_measurement


def test_create_measurement_service(app):
    data = {
        "temperature": 26.5,
        "humidity": 70
    }

    measurement = create_measurement(data)

    assert measurement.id is not None
    assert measurement.temperature == 26.5
    assert measurement.humidity == 70