from app.services.measurement_service import get_latest_measurements

def register_alert_tools(mcp):

    @mcp.tool()
    def detect_extreme_temperature():
        """
        Detect dangerous temperatures.
        """

        data = get_latest_measurements()

        if not data:
            return {
                "status": "no_data"
            }

        latest = data[0]

        if latest.temperature > 35:
            return {
                "alert": True,
                "message": "High temperature detected"
            }

        if latest.temperature < 10:
            return {
                "alert": True,
                "message": "Low temperature detected"
            }

        return {
            "alert": False,
            "message": "Temperature normal"
        }