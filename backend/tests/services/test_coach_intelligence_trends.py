from unittest.mock import Mock, patch

from api.services.coach_intelligence_service import (
    generate_coach_insights,
)


def test_coach_intelligence_includes_improving_trend():
    db = Mock()

    mock_sessions = [
        Mock(
            distance=5.0,
            duration=30.0,
            average_pace=6.0,
            training_load=50,
        ),
    ]

    mock_analysis = Mock(
        risks=[],
        strengths=[],
        recommendations=[],
        total_sessions=1,
        total_distance=5.0,
        total_training_load=50.0,
        average_pace=6.0,
        average_heart_rate=140,
        longest_run=5.0,
    )

    mock_training_repository = Mock()
    mock_training_repository.get_recent_sessions.return_value = (
        mock_sessions
    )

    mock_goal_repository = Mock()
    mock_goal_repository.get_active_goals.return_value = []

    mock_athlete_repository = Mock()
    mock_athlete_repository.get_by_id.return_value = Mock()

    mock_trend_repository = Mock()

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
        "api.services.coach_intelligence_service.ActivityMetricRepository",
        return_value=mock_trend_repository,
    ), patch(
        "api.services.coach_intelligence_service.generate_athlete_performance_trends",
        return_value={
            "distance_trend": "increasing",
            "pace_trend": "improving",
            "training_load_trend": "stable",
        },
    ), patch(
        "api.services.coach_intelligence_service.analyse_training",
        return_value=mock_analysis,
    ):
        result = generate_coach_insights(
            db,
            athlete_id=1,
        )

    assert (
        "Running pace is improving over recent activities."
        in result["insights"]
    )


def test_coach_intelligence_detects_training_load_increase():
    db = Mock()

    mock_training_repository = Mock()
    mock_training_repository.get_recent_sessions.return_value = [
        Mock(
            distance=5.0,
            duration=30.0,
        ),
    ]

    mock_goal_repository = Mock()
    mock_goal_repository.get_active_goals.return_value = []

    mock_athlete_repository = Mock()
    mock_athlete_repository.get_by_id.return_value = Mock()

    mock_analysis = Mock(
        risks=[],
        strengths=[],
        recommendations=[],
        total_sessions=1,
        total_distance=5.0,
        total_training_load=50.0,
        average_pace=6.0,
        average_heart_rate=140,
        longest_run=5.0,
    )

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
        "api.services.coach_intelligence_service.ActivityMetricRepository",
        return_value=Mock(),
    ), patch(
        "api.services.coach_intelligence_service.generate_athlete_performance_trends",
        return_value={
            "distance_trend": "stable",
            "pace_trend": "stable",
            "training_load_trend": "increasing",
        },
    ), patch(
        "api.services.coach_intelligence_service.analyse_training",
        return_value=mock_analysis,
    ):
        result = generate_coach_insights(
            db,
            athlete_id=1,
        )

    assert (
        "Training load is increasing. Monitor fatigue and recovery."
        in result["insights"]
    )
