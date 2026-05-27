import logging

from app.services.measurement_service import (
    get_latest_measurements,
)

logger = logging.getLogger(__name__)


def register_measurement_tools(mcp):

    @mcp.tool()
    def latest_measurements():
        """
        Get latest weather measurements.
        """

        logger.info("Tool latest_measurements called")

        try:

            data = get_latest_measurements()

            result = [
                {
                    "temperature": float(m.temperature),
                    "humidity": float(m.humidity),
                    "created_at": m.created_at.isoformat()
                }
                for m in data
            ]

            logger.info(f"Returning {len(result)} measurements")

            return result

        except Exception as e:

            logger.exception("Error in latest_measurements")

            return {
                "error": str(e)
            }