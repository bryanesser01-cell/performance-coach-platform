from datetime import datetime

from database.activity_models import ActivityMetric
from database.models import Activity
from database.repositories.activity_metric_repository import (
    ActivityMetricRepository,
)


def test_get_by_athlete_id(db_session):
    activity = Activity(
        athlete_id=1,
        source="garmin",
        category="run",
        name="Morning Run",
        started_at=datetime(2026, 7, 28, 6, 0, 0),
        created_at=datetime(2026, 7, 28, 6, 0, 0),
    )

    db_session.add(activity)
    db_session.commit()
    db_session.refresh(activity)

    metric = ActivityMetric(
        activity_id=activity.id,
        distance_km=5,
        duration_seconds=1500,
        average_pace=300,
        training_load=50,
    )

    db_session.add(metric)
    db_session.commit()

    repository = ActivityMetricRepository(
        db_session,
    )

    results = repository.get_by_athlete_id(
        athlete_id=1,
    )

    assert len(results) == 1
    assert results[0].distance_km == 5
