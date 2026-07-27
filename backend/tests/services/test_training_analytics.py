from unittest.mock import Mock, patch

from api.services.training_analytics_service import (
    get_training_summary,
)


def test_get_training_summary():
    db = Mock()

    mock_repository = Mock()

    mock_repository.get_weekly_distance.return_value = 25.0
    mock_repository.get_training_load.return_value = 150.0
    mock_repository.get_recent_sessions.return_value = [
        {
            "distance": 5.0,
            "session_type": "easy",
        }
    ]

    with patch(
        "api.services.training_analytics_service.TrainingRepository",
        return_value=mock_repository,
    ):
        result = get_training_summary(
            db,
            athlete_id=1,
        )

    assert result["athlete_id"] == 1
    assert result["weekly_distance"] == 25.0
    assert result["training_load"] == 150.0
    assert len(result["recent_sessions"]) == 1
