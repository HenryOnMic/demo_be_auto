# FastAPI + MongoDB CRUD Backend

A full-featured backend with FastAPI, MongoDB, Docker, TDD, Swagger UI, and GitHub MCP automation.

## Tech Stack
- FastAPI
- MongoDB 6
- Docker & Docker Compose
- Pytest
- Swagger UI
- GitHub MCP automation

## Features
- Full CRUD for User model (`id`, `name`, `email`, `age`)
- TDD-first: Pytest and FastAPI TestClient
- Pydantic models for all schemas
- OpenAPI docs at `/docs`
- MongoDB test fixtures
- Dockerized for local and CI/CD
- Automated GitHub repo, PR, and CI/CD

## Directory Structure
```
app/
tests/
docker/
.github/workflows/
requirements.txt
README.md
```

## Quick Start
1. Clone repo
2. Run MongoDB via Docker Compose
3. Run tests: `pytest`
4. Start FastAPI: `uvicorn app.main:app --reload`
5. Access docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## Docker
- MongoDB: `localhost:27027` (host), `mongo:27017` (container)
- FastAPI: `localhost:8000`

## GitHub Automation
- Auto-commit, push, PR, and CI/CD via MCP 