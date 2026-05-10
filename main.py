from fastapi import FastAPI
from app import router, stats_router
from app.logger import logger

app = FastAPI(title="Classical Models API")

logger.info("Application started")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Classical Models API!"}

app.include_router(router.router)
app.include_router(stats_router.router)
