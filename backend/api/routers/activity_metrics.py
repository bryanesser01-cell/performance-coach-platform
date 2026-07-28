from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.services.activity_metrics_service import (
    generate_metric_summary,
)
from database.repositories.activity_metric_repository import (
    ActivityMetricRepository,
)
from database.session import get_db

router = APIRouter(
    prefix="/activity-metrics",
    tags=["Activity Metrics"],
)


@router.get("/{activity_id}")
def get_activity_metrics(
    activity_id: int,
    db: Session = Depends(get_db),
):
    repository = ActivityMetricRepository(
        db,
    )

    metric = repository.get_by_activity_id(
        activity_id,
    )

    if metric is None:
        raise HTTPException(
            status_code=404,
            detail="Activity metrics not found",
        )

    return generate_metric_summary(
        metric.distance_km,
        metric.duration_seconds,
        metric.average_heart_rate,
    )
