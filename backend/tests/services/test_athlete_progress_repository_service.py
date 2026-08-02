from unittest.mock import Mock, patch

from api.services.athlete_progress_repository_service import (
    generate_progress_dataset,
)


def test_generate_progress_dataset():

    db = Mock()

    mock_metrics = [
        Mock(
            created_at="2026-01-01",
            average_pace=360,
            distance_km=5.0,
            training_load=50,
        ),
        Mock(
            created_at="2026-01-08",
            average_pace=340,
            distance_km=6.0,
            training_load=60,
        ),
    ]

    mock_repository = Mock()

    mock_repository.get_by_athlete_id.return_value = mock_metrics

    with patch(
        "api.services.athlete_progress_repository_service.ActivityMetricRepository",
        return_value=mock_repository,
    ):

        result = generate_progress_dataset(
            db,
            athlete_id=1,
        )

    assert result["athlete_id"] == 1

    assert result["total_activities"] == 2

    assert result["activities"][0]["pace"] == 360
