from unittest.mock import Mock, patch

from api.services.athlete_progress_repository_service import (
    generate_progress_dataset,
)
from api.services.athlete_progress_timeline_service import (
    generate_progress_timeline,
)


def test_progress_timeline_uses_real_activity_data():

    db = Mock()

    mock_metrics = [
        Mock(
            created_at="2026-01-01",
            average_pace=360,
            distance_km=5.0,
            training_load=50,
        ),
        Mock(
            created_at="2026-02-01",
            average_pace=330,
            distance_km=8.0,
            training_load=80,
        ),
    ]

    repository = Mock()

    repository.get_by_athlete_id.return_value = mock_metrics

    with patch(
        "api.services.athlete_progress_repository_service.ActivityMetricRepository",
        return_value=repository,
    ):

        dataset = generate_progress_dataset(
            db,
            athlete_id=1,
        )

    activities = [
        {
            "pace": activity["pace"],
            "distance_km": activity["distance_km"],
            "training_load": activity["training_load"],
        }
        for activity in dataset["activities"]
    ]

    timeline = generate_progress_timeline(
        activities,
    )

    assert timeline["fitness_trend"] == "improving"

    assert timeline["pace_improvement_seconds_per_km"] == 30

    assert timeline["consistency_score"] == 20


def test_progress_timeline_handles_no_history():

    timeline = generate_progress_timeline(
        [],
    )

    assert timeline["fitness_trend"] == "insufficient_data"

    assert timeline["consistency_score"] == 0
