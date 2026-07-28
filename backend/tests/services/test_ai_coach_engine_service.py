from unittest.mock import Mock, patch

from api.services.ai_coach_engine_service import (
    generate_ai_coach_response,
)


def test_ai_coach_engine_generates_complete_response():

    db = Mock()

    with patch(
        "api.services.ai_coach_engine_service.generate_athlete_performance_report",
        return_value={
            "fitness_status": "progressing",
            "coach_insights": {
                "status": "progressing",
            },
            "race_readiness": {
                "score": 85,
            },
            "race_prediction": {
                "predicted_time_seconds": 1200,
            },
        },
    ):

        result = generate_ai_coach_response(
            db,
            athlete_id=1,
        )

    assert (
        result["athlete_id"]
        == 1
    )

    assert (
        result["athlete_status"]
        == "progressing"
    )

    assert (
        "coach_message"
        in result
    )

    assert (
        "recommendation"
        in result
    )


def test_ai_coach_engine_includes_prediction():

    db = Mock()

    with patch(
        "api.services.ai_coach_engine_service.generate_athlete_performance_report",
        return_value={
            "fitness_status": "progressing",
            "race_prediction": {
                "predicted_time_seconds": 1180,
            },
        },
    ):

        result = generate_ai_coach_response(
            db,
            athlete_id=1,
        )

    assert (
        result["race_prediction"]
        ["predicted_time_seconds"]
        == 1180
    )
