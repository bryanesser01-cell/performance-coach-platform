import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers.athlete import router as athlete_router
from api.routers.auth import router as auth_router
from api.routers.goal import router as goal_router
from api.routers.health import router as health_router
from api.routers.performance_cycles import (
    router as performance_cycle_router,
)
from api.routers.training import router as training_router
from api.routers.workout_plan import router as workout_plan_router
from config.settings import settings
from core.handlers import register_exception_handlers

logging.basicConfig(level=settings.log_level)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown events.
    """
    logger.info("%s starting...", settings.app_name)

    yield

    logger.info("%s shutting down...", settings.app_name)


app = FastAPI(
    title=settings.app_name,
    description="Backend API for the Performance Coach Platform",
    version=settings.app_version,
    lifespan=lifespan,
)

# -----------------------------------------------------
# Exception Handlers
# -----------------------------------------------------

register_exception_handlers(app)

# -----------------------------------------------------
# CORS
# -----------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------
# Root Endpoint
# -----------------------------------------------------


@app.get(
    "/",
    tags=["Root"],
    summary="API Information",
)
def root():
    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "status": "running",
        "health": "/health",
        "docs": "/docs",
    }


# -----------------------------------------------------
# Routers
# -----------------------------------------------------

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(athlete_router)
app.include_router(goal_router)
app.include_router(performance_cycle_router)
app.include_router(training_router)
app.include_router(workout_plan_router)
