# 🌦️ Weather Monitoring API (IoT + Flask)

A backend system for a real-time weather station built with **Flask**, **PostgreSQL**, **Docker**, and **Flask-Migrate**.  
It receives sensor data (Arduino + DHT22), stores it in a database, and exposes REST APIs and an **MCP server** (Model Context Protocol) for AI-assisted monitoring and analytics.

---

# 🚀 Architecture Overview

- Flask → REST API backend  
- PostgreSQL → Time-series data storage  
- SQLAlchemy → ORM  
- Flask-Migrate (Alembic) → Database migrations  
- Docker & Docker Compose → Containerized environment (3 services)  
- MCP Server (FastMCP) → AI-agent interface via stdio, SSE, or Streamable HTTP  
- Arduino / IoT device → Data producer (temperature & humidity)

---

# 📦 Project Structure

```
weather_api/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── schemas/
│   ├── mcp/
│   │   ├── __init__.py
│   │   ├── server.py
│   │   └── tools/
│   │       ├── measurements.py
│   │       ├── statistics.py
│   │       ├── alerts.py
│   │       └── sensors.py
│   ├── extensions.py
│   ├── config.py
│   └── __init__.py
│
├── migrations/
├── tests/
│
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
├── run.py
├── requirements.txt
├── opencode.json
├── AGENTS.md
├── .env.example
└── README.md
```

---

# ⚙️ Environment Variables

Create a `.env` file (local) or `.env.docker` (Docker) based on `.env.example`:

```
FLASK_APP=run.py
FLASK_ENV=development

DATABASE_URL=postgresql://postgres:123456@db:5432/weather_data

POSTGRES_USER=postgres
POSTGRES_PASSWORD=123456
POSTGRES_DB=weather_data
```

---

# 🐳 Run with Docker (Recommended)

## Build and start all services
```bash
docker compose up --build
```

## Check containers
```bash
docker compose ps
```

## Services
| Service | Port  | Description                 |
|---------|-------|-----------------------------|
| web     | 5000  | Flask REST API              |
| mcp     | 8000  | MCP server (Streamable HTTP)|
| db      | 5432  | PostgreSQL 15               |

---

# 🧱 Database Initialization

After first run:
```bash
docker exec -it weather_api bash
flask db upgrade
```

---

# 💻 Run Locally (Without Docker)

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export FLASK_APP=run.py
export DATABASE_URL=postgresql://postgres:123456@localhost/weather_data

# Run migrations
flask db upgrade

# Start Flask API
flask run
```

---

# 📡 REST API Endpoints

## Auth — Login
```
POST /api/login
```
Body:
```json
{
  "username": "admin",
  "password": "your-password"
}
```
Response:
```json
{
  "access_token": "eyJ...",
  "refresh_token": "eyJ..."
}
```

---

## Auth — Refresh Token
```
POST /api/refresh
Authorization: Bearer <refresh_token>
```
Response:
```json
{
  "access_token": "eyJ..."
}
```
The refresh endpoint accepts a valid refresh token and returns a new short-lived access token (1h). Refresh tokens expire after 30 days.

---

## Create Measurement
```
POST /api/measurements
Authorization: Bearer <jwt>
```
Body:
```json
{
  "temperature": 25.5,
  "humidity": 60.2
}
```

---

## Get Latest Measurements
```
GET /api/measurements/latest
Authorization: Bearer <jwt>
```

---

# 🤖 MCP Server

The project includes an **MCP (Model Context Protocol)** server built with [FastMCP](https://github.com/jlowin/fastmcp). It allows AI agents (e.g., OpenCode, Claude, Cursor) to interact with weather data directly.

## Run MCP Server

### Via Docker (Streamable HTTP — port 8000)
Already included in `docker compose up --build`. The `mcp` service runs automatically.

### Via CLI (stdio mode — for local MCP clients)
```bash
python -m app.mcp.server
```

### Via CLI (Streamable HTTP mode — standalone server)
```bash
python -m app.mcp.server streamable-http
```

### Via CLI (SSE mode — legacy)
```bash
python -m app.mcp.server sse
```

## Available MCP Tools

| Tool                        | Description                                          |
|-----------------------------|------------------------------------------------------|
| `latest_measurements`       | Returns the most recent temperature & humidity readings |
| `daily_average_temperature` | Average temperature across all historical records    |
| `daily_average_humidity`    | Average humidity across all historical records       |
| `detect_extreme_temperature`| Alerts if temperature > 35°C or < 10°C               |
| `sensor_status`             | Checks if the sensor sent data within the last 60s   |

## Connect from an MCP Client

### Local (Streamable HTTP — recommended)
```json
{
  "mcp": {
    "weather-station": {
      "type": "streamable-http",
      "url": "http://localhost:8000/mcp",
      "enabled": true
    }
  }
}
```

### Remote (Streamable HTTP)
```json
{
  "mcp": {
    "weather-station-remote": {
      "type": "streamable-http",
      "url": "http://<server-ip>:8000/mcp",
      "enabled": true
    }
  }
}
```

### Local (SSE — legacy)
```json
{
  "mcp": {
    "weather-station": {
      "type": "sse",
      "url": "http://localhost:8000/sse",
      "enabled": true
    }
  }
}
```

---

# 🧪 Testing

```bash
pytest
pytest --cov=app
```

---

# 🐘 Database Details

| Property   | Value                              |
|------------|------------------------------------|
| Host       | `db` (Docker) / `localhost` (local)|
| Port       | 5432 (container) / 5433 (host map) |
| Database   | `weather_data`                     |
| User       | `postgres`                         |
| Password   | `123456`                           |

---

# 🧠 Migrations

```bash
flask db init      # only once
flask db migrate   # generate changes
flask db upgrade   # apply changes
```

---

# 🐳 Docker Services

| Service | Image                        | Command                                     |
|---------|------------------------------|---------------------------------------------|
| web     | weather_monitoring_backend-web | `flask run --host=0.0.0.0`                |
| mcp     | weather_monitoring_backend-mcp | `python -m app.mcp.server streamable-http` |
| db      | postgres:15                    | `postgres`                                 |

---

# 🚀 Future Improvements

- WebSockets real-time dashboard  
- IoT streaming optimization  
- JWT authentication (done)  
- Cloud deployment (AWS / Render / Railway)  
- Grafana monitoring integration  
- MCP tool authentication

---

# 👨‍💻 Author

Rubén Camero
Weather IoT system built with Flask + Arduino + PostgreSQL + MCP