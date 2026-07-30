from fastapi import FastAPI

from api.routers.activity import router as activity_router
from api.routers.activity_metrics import router as activity_metrics_router
from api.routers.ai_coach import router as ai_coach_router_old
from api.routers.ai_coach_chat_router import (
    router as ai_coach_chat_router,
)
from api.routers.ai_coach_conversation import router as ai_coach_conversation_router
from api.routers.analysis import router as analysis_router
from api.routers.analytics import router as analytics_router
from api.routers.athlete import router as athlete_router
from api.routers.athlete_checkin import router as athlete_checkin_router
from api.routers.athlete_dashboard import router as athlete_dashboard_router
from api.routers.athlete_memory import router as athlete_memory_router
from api.routers.athlete_performance import router as athlete_performance_router
from api.routers.athlete_performance_report import (
    router as athlete_performance_report_router,
)
from api.routers.athlete_progress_timeline import (
    router as athlete_progress_timeline_router,
)
from api.routers.coach import router as coach_router
from api.routers.goal import router as goal_router
from api.routers.health import router as health_router
from api.routers.performance import router as performance_router
from api.routers.performance_trends import router as performance_trends_router
from api.routers.recommendation import router as recommendation_router
from api.routers.training import router as training_router
from api.routers.voice_coach import router as voice_coach_router
from api.routers.workout import router as workout_router
from api.routes.ai_coach_routes import router as ai_coach_router

app = FastAPI(
    title="Performance Coach API",
    version="1.0.0",
)


# Core routers
app.include_router(health_router)

app.include_router(activity_router)
app.include_router(activity_metrics_router)

app.include_router(athlete_router)
app.include_router(athlete_checkin_router)
app.include_router(athlete_dashboard_router)
app.include_router(athlete_memory_router)
app.include_router(athlete_performance_router)
app.include_router(athlete_performance_report_router)
app.include_router(athlete_progress_timeline_router)
app.include_router(
    ai_coach_chat_router,
)

app.include_router(goal_router)

app.include_router(training_router)
app.include_router(workout_router)

app.include_router(performance_router)
app.include_router(performance_trends_router)

app.include_router(analysis_router)
app.include_router(analytics_router)

app.include_router(coach_router)
app.include_router(recommendation_router)

app.include_router(voice_coach_router)

# Existing AI Coach routers
app.include_router(ai_coach_router_old)
app.include_router(ai_coach_conversation_router)

# New AI Coach production route
app.include_router(ai_coach_router)


@app.get("/")
def root():
    return {
        "message": "Performance Coach API running",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "performance-coach-api",
    }
