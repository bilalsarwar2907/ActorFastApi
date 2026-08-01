# ActorFastApi — Claude Context

## What This Project Is
Python REST API built to learn FastAPI by mapping C# .NET patterns.
- Live: https://actorfastapi.onrender.com/docs
- GitHub: https://github.com/bilalsarwar2907/ActorFastApi
- Local port: **8001** (8000 is taken by ai-cost-router)

## Run Commands
```bash
python -m uvicorn main:app --reload --port 8001   # run locally
python -m pytest tests/test_actors.py -v          # run tests
docker-compose up --build                          # run in Docker with PostgreSQL
```

## Architecture
- Interface/repository pattern — `IActorRepository` (ABC) with `ActorDbRepository` (active)
- Dependency injection via `Depends()` — mirrors C# `services.AddScoped<>()`
- JWT auth on POST/PUT/DELETE — `Depends(get_current_user)`
- SQLite locally, PostgreSQL on Render — switches automatically via `DATABASE_URL` env var

## Non-Negotiable Rules
1. Always use `python -m` prefix — never bare `uvicorn` or `pytest`
2. Any `pip install` → immediately add to `requirements.txt`
3. Login endpoint uses **form data** (`data={}`), register uses **JSON** (`json={}`) — never mix
4. `bcrypt==4.0.1` must stay pinned in `ci.yml` — passlib 1.7.4 breaks with newer versions
5. `tests/__init__.py` must exist — empty file, required for pytest on Linux/CI
6. Never hardcode packages in `ci.yml` — always `pip install -r requirements.txt`

## Known Pitfalls (Do Not Repeat)
- `postgres://` → must be rewritten to `postgresql://` (handled in database.py)
- `check_same_thread` arg only for SQLite, not PostgreSQL (handled in database.py)
- `python-multipart` must be in requirements.txt or login crashes on Render
- New files created via shell may be empty — always verify content before running tests

## Current State
✅ REST API + SQLAlchemy ORM  
✅ JWT Authentication  
✅ GitHub Actions CI (8/8 tests passing)  
✅ Render deployment (PostgreSQL)  
✅ Docker (Dockerfile + docker-compose with PostgreSQL)  

## What's Next
- Improve tests — edge cases (duplicate id, get non-existent id)
- Switch database demo — show in-memory vs SQLite vs PostgreSQL swap
