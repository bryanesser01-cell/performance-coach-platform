from unittest.mock import Mock, patch

from api.services.coach_intelligence_service import (
    generate_coach_insights,
)


def test_generate_coach_insights_with_training_data():
    db = Mock()

    mock_sessions = [
        Mock(
            distance=5.0,
            duration=30.0,
            average_pace=6.0,
            average_hr=140,
            max_hr=160,
            cadence=170,
            elevation_gain=50,
            training_load=50,
            rpe=5,
        ),
        Mock(
            distance=8.0,
            duration=40.0,
            average_pace=5.0,
            average_hr=150,
            max_hr=170,
            cadence=175,
            elevation_gain=70,
            training_load=80,
            rpe=6,
        ),
    ]

    mock_analysis = Mock(
        risks=[],
        strengths=[
            "Training consistency is improving.",
        ],
        recommendations=[
            "Continue building consistently.",
        ],
        total_sessions=2,
        total_distance=13.0,
        total_training_load=130.0,
        average_pace=5.5,
        average_heart_rate=145,
        longest_run=8.0,
    )

    mock_training_repository = Mock()
    mock_training_repository.get_recent_sessions.return_value = mock_sessions

    mock_goal_repository = Mock()
    mock_goal_repository.get_active_goals.return_value = []

    mock_athlete_repository = Mock()
    mock_athlete_repository.get_by_id.return_value = Mock()

    with patch(
        "api.services.coach_intelligence_service.TrainingRepository",
        return_value=mock_training_repository,
    ), patch(
        "api.services.coach_intelligence_service.GoalRepository",
        return_value=mock_goal_repository,
    ), patch(
        "api.services.coach_intelligence_service.AthleteRepository",
        return_value=mock_athlete_repository,
    ), patch(
        "api.services.coach_intelligence_service.analyse_training",
        return_value=mock_analysis,
    ):
        result = generate_coach_insights(
            db,
            athlete_id=1,
        )

    assert result["athlete_id"] == 1
    assert result["status"] == "progressing"
    assert "metrics" in result
    assert "goals" in result
    assert "insights" in result
    assert "recommendations" in result


def test_generate_coach_insights_without_training_data():
    db = Mock()

    mock_training_repository = Mock()
    mock_training_repository.get_recent_sessions.return_value = []

    with patch(
        "api.services.coach_intelligence_service.TrainingRepository",
        return_value=mock_training_repository,
    ):
        result = generate_coach_insights(
            db,
            athlete_id=1,
        )

    assert result["athlete_id"] == 1
    assert result["status"] == "insufficient_data"
    assert result["goals"] == []
    assert len(result["insights"]) > 0
