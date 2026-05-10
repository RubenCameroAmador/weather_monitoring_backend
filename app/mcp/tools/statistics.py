from app.models.measurement import Measurement
from app.extensions import db
from sqlalchemy import func

def register_statistics_tools(mcp):

    @mcp.tool()
    def daily_average_temperature():
        """
        Get average daily temperature.
        """

        avg = db.session.query(
            func.avg(Measurement.temperature)
        ).scalar()

        return {
            "average_temperature": round(avg or 0, 2)
        }

    @mcp.tool()
    def daily_average_humidity():
        """
        Get average daily humidity.
        """

        avg = db.session.query(
            func.avg(Measurement.humidity)
        ).scalar()

        return {
            "average_humidity": round(avg or 0, 2)
        }