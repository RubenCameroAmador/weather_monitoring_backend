from app.services.measurement_service import (
    get_latest_measurements,
)

def register_measurement_tools(mcp):

    @mcp.tool()
    def latest_measurements():
        """
        Get latest weather measurements.
        """

        data = get_latest_measurements()

        return [
            {
                "temperature": m.temperature,
                "humidity": m.humidity,
                "created_at": str(m.created_at)
            }
            for m in data
        ]