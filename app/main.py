from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="F1 Data Aggregation Service",
    description="Backend service aggregating Formula 1 data from public API",
    version="0.1.0"
)

app.include_router(health_router)
