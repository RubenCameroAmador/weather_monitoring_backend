# AGENTS.md

## Commands

| Purpose | Command |
|---|---|
| Serve app | `flask run` or `python run.py` |
| Run tests | `pytest` (or `pytest --cov=app`) |
| Apply migrations | `flask db upgrade` |
| Docker | `docker compose up --build` |
| Run MCP server | `python -m app.mcp.server` |

## Architecture

- **App factory** in `app/__init__.py`; tests create their own app via `create_app({...overrides...})`.
- **3 blueprints** under `/api`: `measurement`, `user`, `auth`.
- **Services layer** in `app/services/` — routes delegate business logic here.
- **MCP server** uses `fastmcp` and runs inside `flask_app.app_context()`. Registered in `opencode.json` as a local command.
- **No frontend** — pure API backend + MCP.

## Quirks

- **JWT required** on `POST /api/measurements` and `GET /api/measurements/latest`. The only unauthenticated measurement endpoint is `GET /api/ping`.
- **DB port mapping**: host `5433` → container `5432` (non-standard).
- **Two `.env` files**: `.env` (local) and `.env.docker` (Docker). Both are gitignored.
- **`daily_average_temperature` / `daily_average_humidity`**: compute AVG over **all** historical records, not just today.
- **Tests** use SQLite `:memory:` with `db.create_all()` — no PostgreSQL needed.
- **No linter, formatter, typechecker, pre-commit, or CI** configured in this repo.
