from app.extensions import db
from datetime import datetime, UTC

class Measurement(db.Model):
    __tablename__ = "measurements"

    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(50), default="arduino_1")
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )

    def __repr__(self):
        return f"<Measurement {self.temperature}°C>"