from app.services.measurement_service import get_latest_measurements
from datetime import datetime, timezone

def register_sensor_tools(mcp):

    @mcp.tool()
    def sensor_status():
        """
        Check if sensor is online.
        """

        data = get_latest_measurements()

        if not data:
            return {
                "online": False,
                "message": "No measurements found"
            }

        latest = data[0]

        delta = datetime.now(timezone.utc) - latest.created_at

        online = delta.total_seconds() < 60

        return {
            "online": online,
            "last_measurement": str(latest.created_at)
        }