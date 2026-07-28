from database.activity_models import ActivityMetric
from database.repositories.activity_metric_repository import (
    ActivityMetricRepository,
)


def test_create_activity_metric(db_session):
    repository = ActivityMetricRepository(
        db_session,
    )

    metric = ActivityMetric(
        activity_id=1,
        distance_km=5.0,
        duration_seconds=1500,
        average_pace=300,
        average_heart_rate=150,
        max_heart_rate=175,
        cadence=170,
        elevation_gain=50,
        calories=400,
        training_load=75,
    )

    result = repository.create_metric(
        metric,
    )

    assert result.id is not None
    assert result.distance_km == 5.0


def test_get_activity_metric_by_activity_id(db_session):
    repository = ActivityMetricRepository(
        db_session,
    )

    metric = ActivityMetric(
        activity_id=10,
        distance_km=10.0,
        duration_seconds=3000,
    )

    repository.create_metric(
        metric,
    )

    result = repository.get_by_activity_id(
        10,
    )

    assert result is not None
    assert result.activity_id == 10
    assert result.distance_km == 10.0
