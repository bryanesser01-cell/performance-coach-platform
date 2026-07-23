from fastapi import FastAPI

from config.settings import settings
from core.logging import configure_logging
from core.handlers import register_exception_handlers

configure_logging()

from api.routers.health import router as health_router
from api.routers.athlete import router as athlete_router
from api.routers.goal import router as goal_router
from api.routers.training import router as training_router
from api.routers.analysis import router as analysis_router
from api.routers.workout import router as workout_router
from api.routers.recommendation import router as recommendation_router
from api.routers.coach import router as coach_router
from api.routers.auth import router as auth_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

register_exception_handlers(app)

# Register API Routers
app.include_router(health_router)
app.include_router(athlete_router)
app.include_router(goal_router)
app.include_router(training_router)
app.include_router(analysis_router)
app.include_router(workout_router)
app.include_router(recommendation_router)
app.include_router(coach_router)
app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": f"{settings.app_name} is running!"
    }