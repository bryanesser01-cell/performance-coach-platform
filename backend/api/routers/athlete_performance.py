from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.athlete_performance_summary_service import (
    generate_athlete_performance_summary,
)
from database.repositories.activity_metric_repository import (
    ActivityMetricRepository,
)
from database.session import get_db

router = APIRouter(
    prefix="/athletes",
    tags=["Athlete Performance"],
)


@router.get("/{athlete_id}/performance-summary")
def get_performance_summary(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    """
    Generate athlete performance summary from stored activity metrics.
    """

    repository = ActivityMetricRepository(
        db,
    )

    summary = generate_athlete_performance_summary(
        athlete_id,
        repository,
    )

    return {
        "athlete_id": athlete_id,
        **summary,
    }
