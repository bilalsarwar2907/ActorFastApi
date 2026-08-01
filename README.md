# ActorFastApi

A REST API built with Python and FastAPI, mirroring C# .NET patterns. Built as a learning project to map familiar C# concepts (controllers, repositories, EF, JWT auth) to their Python equivalents.

**Live:** https://actorfastapi.onrender.com/docs  
**Repo:** https://github.com/bilalsarwar2907/ActorFastApi

---

## Features

- Full CRUD REST API for actors
- SQLAlchemy ORM with interface/repository pattern (3 implementations: in-memory, SQLite, PostgreSQL)
- JWT Authentication — register, login, protected routes
- Auto-switches between SQLite (local) and PostgreSQL (production/Docker)
- Docker support (Dockerfile + docker-compose with PostgreSQL)
- GitHub Actions CI — 8/8 tests passing on every push
- Auto-deploy to Render on push to `master`
- Claude Code integration — hooks auto-run tests after every `.py` edit

---

## Getting Started

### Prerequisites

- Python 3.11+
- pip

### Run Locally

```bash
# Install dependencies
pip install -r requirements.txt
pip install bcrypt==4.0.1

# Start the server (port 8001 — port 8000 may be taken)
python -m uvicorn main:app --reload --port 8001
```

API docs available at: http://localhost:8001/docs

### Run Tests

```bash
python -m pytest tests/test_actors.py -v
```

### Run with Docker

```bash
docker-compose up --build
```

This spins up the app + a PostgreSQL container. App runs on port 8001.

---

## Project Structure

```
ActorFastApi/
├── main.py                          # App entry point
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── ci.yml                   # GitHub Actions CI
├── auth/
│   └── auth.py                      # JWT: hash, verify, create token, get_current_user
├── database/
│   └── database.py                  # SQLAlchemy engine + session (auto-switches DB)
├── models/
│   ├── actor.py                     # Pydantic schema (request/response)
│   ├── actor_entity.py              # SQLAlchemy entity (actors table)
│   ├── user.py                      # Pydantic schema for auth
│   └── user_entity.py              # SQLAlchemy entity (users table)
├── interfaces/
│   └── i_actor_repository.py        # ABC interface
├── repositories/
│   ├── actor_repository.py          # In-memory implementation
│   └── actor_db_repository.py       # SQLite/PostgreSQL implementation (active)
├── routers/
│   ├── actor_router.py              # Actor endpoints
│   └── auth_router.py               # Register + Login endpoints
└── tests/
    ├── __init__.py
    └── test_actors.py               # 8 tests covering all endpoints + auth
```

---

## API Endpoints

### Auth

| Method | Endpoint | Body | Auth |
|--------|----------|------|------|
| POST | `/auth/register` | `{"username": "", "password": ""}` (JSON) | None |
| POST | `/auth/login` | `username=&password=` (form data) | None |

### Actors

| Method | Endpoint | Auth |
|--------|----------|------|
| GET | `/actors/` | None |
| GET | `/actors/{id}` | None |
| POST | `/actors/` | Bearer token required |
| PUT | `/actors/{id}` | Bearer token required |
| DELETE | `/actors/{id}` | Bearer token required |

---

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection string | `sqlite:///./actors.db` |

Set `DATABASE_URL` to a PostgreSQL URL for production. The app handles the `postgres://` → `postgresql://` format fix automatically.

---

## Deployment (Render)

- Web Service: https://actorfastapi.onrender.com
- PostgreSQL on Render free tier (expires after 90 days)
- Auto-deploys on push to `master`
- Cold start: ~50 seconds on free tier
- Set `DATABASE_URL` env var to the Internal Database URL from Render PostgreSQL dashboard

---

## C# → Python Mapping

| C# | Python |
|----|--------|
| `class Actor` with properties | `class Actor(BaseModel)` — Pydantic |
| `interface IActorRepository` | `class IActorRepository(ABC)` |
| `DbContext` | SQLAlchemy `Session` + `Base` |
| Entity Framework entity | `ActorEntity(Base)` with `Column()` |
| `IActionResult` controller | FastAPI `APIRouter` endpoint functions |
| `services.AddScoped<>()` | `Depends(get_repo)` |
| `[Authorize]` attribute | `Depends(get_current_user)` parameter |
| `BCrypt.Net.HashPassword()` | `pwd_context.hash()` (passlib) |
| `JwtSecurityTokenHandler` | `jose.jwt.encode()` / `jose.jwt.decode()` |
| `Program.cs` | `main.py` |
| Swagger (Swashbuckle) | Built into FastAPI at `/docs` |
| EF Migrations | `Base.metadata.create_all()` |
| `using (var db = new DbContext())` | `yield db` in `get_db()` |

---

## Known Gotchas

- **Login uses form data, not JSON.** `POST /auth/login` expects `application/x-www-form-urlencoded`, not `application/json`.
- **bcrypt must be pinned** to `4.0.1` — newer versions break passlib in CI.
- **Docker CMD must use `--host 0.0.0.0`** or the app is unreachable from outside the container.
- **`tests/__init__.py` must exist** for pytest to work on Linux/CI.
- **`actors.db` is gitignored** — do not commit the SQLite file.

---

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [passlib](https://passlib.readthedocs.io/) + [python-jose](https://python-jose.readthedocs.io/) — JWT auth
- [pytest](https://pytest.org/) + [httpx](https://www.python-httpx.org/) — testing
- [Docker](https://www.docker.com/) — containerization
- [Render](https://render.com/) — hosting
- [GitHub Actions](https://github.com/features/actions) — CI
