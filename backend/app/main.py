from fastapi import FastAPI

from api.routers.auth import router as auth_router
from api.routers.athlete import router as athlete_router
from api.routers.health import router as health_router

app = FastAPI(
    title="Performance Coach Platform API",
    description="Backend API for the Performance Coach Platform",
    version="1.0.0",
)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Performance Coach Platform API",
        "status": "running",
        "health": "/health",
        "docs": "/docs",
    }


app.include_router(health_router)
app.include_router(auth_router)
app.include_router(athlete_router)