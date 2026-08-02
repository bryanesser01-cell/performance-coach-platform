from unittest.mock import Mock, patch

from api.services.athlete_training_plan_service import (
    generate_athlete_training_plan,
)


def test_generate_athlete_training_plan():

    db = Mock()

    with patch(
        "api.services.athlete_training_plan_service.generate_coach_insights",
        return_value={
            "status": "progressing",
            "performance_trends": {
                "training_load_trend": "stable",
            },
            "coach_recommendation": {
                "recommendation": "continue_progression",
            },
        },
    ):
        result = generate_athlete_training_plan(
            db,
            athlete_id=1,
        )

    assert result["athlete_id"] == 1

    assert result["coach_recommendation"]["recommendation"] == "continue_progression"

    assert (
        len(
            result["training_plan"]["weekly_sessions"],
        )
        == 3
    )


def test_training_plan_uses_training_load_trend():

    db = Mock()

    with patch(
        "api.services.athlete_training_plan_service.generate_coach_insights",
        return_value={
            "status": "progressing",
            "performance_trends": {
                "training_load_trend": "increasing",
            },
            "coach_recommendation": {},
        },
    ):
        result = generate_athlete_training_plan(
            db,
            athlete_id=1,
        )

    sessions = result["training_plan"]["weekly_sessions"]

    assert sessions[1]["workout"] == "Threshold Session"
