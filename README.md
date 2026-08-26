# pg-admin

A learning project to understand how a PostgreSQL database management workflow works end-to-end, built with **Python** and **FastAPI**, exposing CRUD (Create, Read, Update, Delete) operations against a PostgreSQL database.

## Purpose

This repo exists to explore and document the backend workflow behind managing a Postgres database via an API layer — connection handling, schema/models, and standard CRUD endpoints.

## Tech Stack

- **Python 3**
- **FastAPI** — web framework for the CRUD API
- **PostgreSQL** — database
- (Planned) an ORM/driver such as SQLAlchemy or asyncpg for DB access

## Project Status

Early stage / work in progress.

## Getting Started

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies (once requirements.txt is added)
pip install -r requirements.txt
```

## Repository Notes

- `venv/` and other local/environment artifacts are excluded via `.gitignore` and are not tracked in this repo.
