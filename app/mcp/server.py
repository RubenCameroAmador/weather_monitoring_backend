from app import create_app
from fastmcp import FastMCP

from app.mcp.tools.measurements import (
    register_measurement_tools
)

from app.mcp.tools.statistics import (
    register_statistics_tools
)

from app.mcp.tools.alerts import (
    register_alert_tools
)

from app.mcp.tools.sensors import (
    register_sensor_tools
)

flask_app = create_app()

mcp = FastMCP("Weather Station MCP")

register_measurement_tools(mcp)
register_statistics_tools(mcp)
register_alert_tools(mcp)
register_sensor_tools(mcp)

if __name__ == "__main__":

    with flask_app.app_context():
        mcp.run()