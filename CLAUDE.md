# pg-admin — Project Memory

## What this project is
A production-grade PostgreSQL database management tool. Backend is Python + FastAPI,
exposing CRUD operations against Postgres. This is explicitly NOT a toy/demo — built
with production intent from the first file.

## Repo
- GitHub: https://github.com/viplav-artha/pg-admin (public, personal account `viplav-artha`, no org)
- Local path: /Users/viplavsingh/Desktop/project/pg-admin
- **All work (commits/pushes) happens on the `claude` branch, never directly on
  `main`.** PR #1 (`claude` -> `main`) has already been merged once; that does
  NOT mean it's now safe to commit to `main` — stay on `claude`, and open a new
  PR when the next batch of work is ready to merge. Before any commit, confirm
  with `git status`/`git branch` that the checked-out branch is `claude`, not
  `main`.

## How this project is being taught/built (rules for any session, including a fresh one)
- Teacher/student mode. Before writing any new file: explain WHY the file needs to
  exist and WHAT logic goes in it, in plain language, as if teaching someone new to
  Python. Analogies are fine in chat explanations.
- One file at a time. Do not start the next file until the user has studied the
  current one and explicitly says they're ready to move on.
- After every file is created: update this file's "Current status" and
  "Files created so far" sections, AND add a matching entry to NOTES.md
  (timeline graph + logic/motive note, no analogies in NOTES.md).
- Repo is PUBLIC — never put real secrets/credentials in any tracked file
  (`.env` stays git-ignored; only `.env.example` with placeholders is committed).

## Current status
Stage: Lesson 8 complete — Alembic migrations wired up (`alembic.ini`,
`alembic/env.py`), and `app/main.py` updated to drop `create_all()` now that
Alembic owns schema changes. Dependencies installed into `venv` (pip install
ran successfully). Waiting on user's next direction — no lesson queued yet.
The user has NOT yet run `alembic revision --autogenerate` / `alembic
upgrade head` against a real Postgres instance (needs one running that
matches `.env`).

Run the app: `source venv/bin/activate && uvicorn app.main:app --reload`,
then visit `http://127.0.0.1:8000/docs`. Run migrations:
`alembic revision --autogenerate -m "..."` then `alembic upgrade head`.

## Known production gaps (flagged, not yet fixed)
- No authentication/authorization on any endpoint yet.
- No automated tests yet.

## Planned build order
1. `config.py` — settings/env management — **DONE**
2. `database.py` — SQLAlchemy engine/session, connection handling — **DONE**
3. `models.py` — DB table definitions (SQLAlchemy models) — **DONE** (`Item` model)
4. `schemas.py` — Pydantic request/response schemas — **DONE**
5. `crud.py` — CRUD logic functions — **DONE**
6. `app/routers/items.py` — FastAPI route handlers for `/items` — **DONE**
7. `main.py` — FastAPI app entrypoint, mounts the router — **DONE**
8. Alembic migrations (`alembic.ini`, `alembic/env.py`) — **DONE**
9. (unplanned yet) — auth, tests, etc. — see "Known production gaps" above

## Files created so far (chronological)
1. `.gitignore` — excludes `venv/`, `.env`, caches, IDE files, logs
2. `README.md` — project overview and setup instructions
3. `requirements.txt` — currently: `pydantic-settings`, `python-dotenv`
   (will grow: `fastapi`, `uvicorn`, `sqlalchemy`, `psycopg2-binary`, etc. added
   only when the lesson that needs them is reached)
4. `.env.example` — template env vars, committed, placeholder values only
5. `.env` — actual local env vars, git-ignored, not committed
6. `app/__init__.py` — marks `app/` as a Python package
7. `app/core/__init__.py` — marks `app/core/` as a Python package
8. `app/core/config.py` — `Settings` class (pydantic-settings) + cached
   `get_settings()`; builds `database_url` from `POSTGRES_*` env vars
9. `app/core/database.py` — SQLAlchemy `engine` + `SessionLocal` factory +
   `Base` declarative class + `get_db()` dependency generator. Imports
   `get_settings` from `app/core/config.py`.
10. `app/models.py` — `Item` SQLAlchemy model (table `items`): `id`, `name`,
    `description`, `created_at`, `updated_at`. Imports `Base` from
    `app/core/database.py`.
11. `app/schemas.py` — Pydantic API schemas: `ItemBase`, `ItemCreate`,
    `ItemUpdate`, `ItemRead`. Deliberately does not import from
    `app/models.py` or `app/core/database.py` — the API shape is kept
    independent of the DB layer.
12. `app/crud.py` — pure DB-operation functions (`get_item`, `get_items`,
    `create_item`, `update_item`, `delete_item`), each taking a `Session`
    explicitly. Imports from both `app/models.py` and `app/schemas.py`
    (first fan-in in the project).
13. `app/routers/__init__.py` — marks `app/routers/` as a Python package
    (plumbing, excluded from Routes Graph).
14. `app/routers/items.py` — FastAPI `APIRouter` with full CRUD endpoints
    (`POST /items/`, `GET /items/`, `GET /items/{id}`, `PATCH /items/{id}`,
    `DELETE /items/{id}`). Imports from `app/crud.py`, `app/schemas.py`, and
    `app/core/database.py` (`get_db`) — a three-way fan-in.
15. `app/main.py` — creates the `FastAPI` app instance, mounts
    `items.router`, and adds a `/health` endpoint. This is the file
    `uvicorn` actually runs.
16. `alembic.ini` + `alembic/env.py` (scaffolded via `alembic init alembic`,
    then edited) — versioned schema migrations, replacing `create_all()`.
    `env.py` imports `app.models` (to register `Item` on `Base.metadata`),
    `get_settings`, and `Base`; overrides `sqlalchemy.url` at runtime from
    `.env` instead of duplicating it in `alembic.ini`.
17. `app/main.py` revised — removed `Base.metadata.create_all(bind=engine)`
    and the now-unused `Base`/`engine` import, since Alembic now owns schema
    creation exclusively.

## Environment
- Python venv at `./venv` — activate with `source venv/bin/activate`
- Install deps: `pip install -r requirements.txt`
- Editor may show an unresolved-import warning for `pydantic_settings` in
  `config.py` until deps are installed inside the venv — expected, not a bug.

## Companion file
See `NOTES.md` for the plain-language, no-analogy study notes and the visual
file-creation timeline.

## Maintenance instructions — MUST run after every new file is created
These steps are not optional and must happen every single time a new project
file is created, before moving on to the next lesson:

1. **Update `CLAUDE.md`** (this file):
   - Update "Current status" to reflect the new file and what's next.
   - Move the completed item's build-order entry to done, and mark the new
     next item.
   - Append the new file to "Files created so far" with a one-line description.
2. **Update `NOTES.md` — Timeline graph**:
   - Append the new file as the next node, connected with `|` / `v` to the
     previous node. This graph includes ALL files, no exceptions, in strict
     creation order.
3. **Update `NOTES.md` — Routes Graph**:
   - Only touch this graph if the new file contains actual import-relevant
     logic. Skip it for `.gitignore`, `.env`/`.env.example`, README,
     `requirements.txt`, and empty `__init__.py` files.
   - This is a **Mermaid** (` ```mermaid graph TD `) diagram — GitHub/VS Code
     render it as a real flowchart. There is exactly ONE Routes Graph diagram
     in NOTES.md. Add the new node and its edges to that SAME diagram in
     place — never create a second Routes Graph elsewhere in the file.
   - Assign the new node the next number in the Routes Graph's own sequence
     (independent from the Timeline number — NOTES.md already explains the
     two numbering systems are different), as part of its node label, e.g.
     `n9["[9] filename"]`.
   - Label each new edge with *what* it imports, e.g. `n2 -->|get_db| n6` —
     this replaces needing a separate connections list, since Mermaid edge
     labels carry that information directly in the diagram.
4. **Update `NOTES.md` — File notes**:
   - Add a new `### [N] filename` entry with a `Motive` line and a `Logic`
     line. No analogies, no fluff — short and factual.

Do all four updates every time, without waiting to be asked again.
