# 🌦️ Weather Monitoring API (IoT + Flask)

A backend system for a real-time weather station built with **Flask**, **PostgreSQL**, **Docker**, and **Flask-Migrate**.  
It receives sensor data (Arduino + DHT22), stores it in a database, and exposes REST APIs for monitoring and analytics.

---

# 🚀 Architecture Overview

- Flask → REST API backend  
- PostgreSQL → Time-series data storage  
- SQLAlchemy → ORM  
- Flask-Migrate (Alembic) → Database migrations  
- Docker & Docker Compose → Containerized environment  
- Arduino / IoT device → Data producer (temperature & humidity)

---

# 📦 Project Structure

weather_api/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── schemas/
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
├── .env.example
└── README.md

---

# ⚙️ Environment Variables

Create a `.env` file based on `.env.example`:

FLASK_APP=run.py  
FLASK_ENV=development  

DATABASE_URL=postgresql://postgres:123456@db:5432/weather_data  

POSTGRES_USER=postgres  
POSTGRES_PASSWORD=123456  
POSTGRES_DB=weather_data  

---

# 🐳 Run with Docker (Recommended)

## Build and start services
docker compose up --build

## Check containers
docker compose ps

## API runs at
http://localhost:5000/api

---

# 🧱 Database Initialization

After first run:

docker exec -it weather_api bash
flask db upgrade

---

# 💻 Run Locally (Without Docker)

## Create virtual environment
python3 -m venv .venv  
source .venv/bin/activate  

## Install dependencies
pip install -r requirements.txt  

## Set environment variables
export FLASK_APP=run.py  
export DATABASE_URL=postgresql://postgres:123456@localhost/weather_data  

## Run migrations
flask db upgrade  

## Start server
flask run  

---

# 📡 API Endpoints

## Health Check
GET /api/ping

Response:
{
  "message": "pong"
}

---

## Create Measurement
POST /api/measurements

Body:
{
  "temperature": 25.5,
  "humidity": 60.2
}

---

## Get Latest Measurements
GET /api/measurements/latest

---

# 🧪 Testing

Run tests:
pytest  

With coverage:
pytest --cov=app  

---

# 🐘 Database Details

Host: db (Docker)  
Port: 5432  
Database: weather_data  

---

# 🧠 Migrations

flask db init      # only once  
flask db migrate   # generate changes  
flask db upgrade   # apply changes  

---

# 🐳 Docker Services

Service: web → Flask API  
Service: db  → PostgreSQL 15  

---

# ⚠️ Important Notes

- Do NOT commit `.env`
- Use `.env.example` as reference
- Do NOT run `flask db init` in production
- Use `entrypoint.sh` for automatic startup in Docker

---

# 🚀 Future Improvements

- WebSockets real-time dashboard  
- IoT streaming optimization  
- JWT authentication  
- Cloud deployment (AWS / Render / Railway)  
- Grafana monitoring integration  

---

# 👨‍💻 Author

Weather IoT system built with Flask + Arduino + PostgreSQL