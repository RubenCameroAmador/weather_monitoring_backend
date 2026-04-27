from app.extensions import db
from app.models.measurement import Measurement

def create_measurement(data):
    measurement = Measurement(
        temperature=data["temperature"],
        humidity=data["humidity"],
        device_id=data.get("device_id", "arduino_1")
    )

    db.session.add(measurement)
    db.session.commit()

    return measurement


def get_latest_measurements(limit=10):
    return Measurement.query.order_by(
        Measurement.created_at.desc()
    ).limit(limit).all()