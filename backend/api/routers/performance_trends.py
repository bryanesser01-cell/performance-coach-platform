from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.performance_trend_service import (
    generate_athlete_performance_trends,
)
from database.repositories.activity_metric_repository import (
    ActivityMetricRepository,
)
from database.session import get_db

router = APIRouter(
    prefix="/athletes",
    tags=["Performance Trends"],
)


@router.get("/{athlete_id}/performance-trends")
def get_performance_trends(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    """
    Generate athlete performance trends from stored activity metrics.
    """

    repository = ActivityMetricRepository(
        db,
    )

    trends = generate_athlete_performance_trends(
        athlete_id,
        repository,
    )

    return {
        "athlete_id": athlete_id,
        **trends,
    }
