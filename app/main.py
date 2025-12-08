from fastapi import FastAPI

app = FastAPI(
    title="F1 Data Aggregation Service",
    description="Backend service aggregating Formula 1 data from public API",
    version="0.1.0"
)

@app.get('/health')
def health_check():
    return {"status": "ok"}
