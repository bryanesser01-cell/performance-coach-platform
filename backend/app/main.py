from fastapi import FastAPI

from api.routers.health import router as health_router
from api.routers.athlete import router as athlete_router

app = FastAPI(
    title="Performance Coach API",
    version="0.1.0",
)

app.include_router(health_router)
app.include_router(athlete_router)

@app.get("/")
def root():
    return {
        "message": "Performance Coach API is running!"
    }
