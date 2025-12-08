# F1 Data Aggregation Service

Backend service that aggregates Formula 1 data from a public API and exposes it via REST endpoints.

## Tech stack
- Python 3.11
- FastAPI
- Docker

## Run locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
## Run with Docker
```bash
docker compose up
```
