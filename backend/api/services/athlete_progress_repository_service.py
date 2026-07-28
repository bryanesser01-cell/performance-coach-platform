from sqlalchemy.orm import Session

from database.repositories.activity_metric_repository import (
    ActivityMetricRepository,
)


def get_athlete_progress_history(
    db: Session,
    athlete_id: int,
) -> list[dict]:
    """
    Retrieve athlete historical performance data
    from stored activity metrics.
    """

    repository = ActivityMetricRepository(
        db,
    )

    metrics = repository.get_by_athlete_id(
        athlete_id,
    )

    return [
        {
            "date": metric.created_at,
            "pace": metric.average_pace or 0.0,
            "distance_km": metric.distance_km or 0.0,
            "training_load": metric.training_load or 0.0,
        }
        for metric in metrics
    ]


def generate_progress_dataset(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Create timeline dataset for athlete.
    """

    history = get_athlete_progress_history(
        db,
        athlete_id,
    )

    return {
        "athlete_id": athlete_id,
        "activities": history,
        "total_activities": len(history),
    }
