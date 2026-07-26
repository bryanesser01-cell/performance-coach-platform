from fastapi import FastAPI

from api.routers.analysis import router as analysis_router
from api.routers.athlete import router as athlete_router
from api.routers.coach import router as coach_router
from api.routers.goal import router as goal_router
from api.routers.health import router as health_router
from api.routers.recommendation import router as recommendation_router
from api.routers.training import router as training_router
from api.routers.workout import router as workout_router
from core.handlers import register_exception_handlers
from core.logging import configure_logging

configure_logging()

app = FastAPI(
    title="Performance Coach API",
    version="0.1.0",
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


@app.get("/")
def root():
    return {
        "message": "Performance Coach API is running!"
    }
