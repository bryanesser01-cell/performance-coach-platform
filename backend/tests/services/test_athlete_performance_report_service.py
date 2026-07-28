from unittest.mock import Mock, patch

from api.services.athlete_performance_report_service import (
    generate_athlete_performance_report,
)


def test_generate_complete_athlete_report():

    db = Mock()

    with patch(
        "api.services.athlete_performance_report_service.generate_coach_insights",
        return_value={
            "status": "progressing",
        },
    ), patch(
        "api.services.athlete_performance_report_service.generate_athlete_training_plan",
        return_value={
            "training_plan": "weekly",
        },
    ):

        result = generate_athlete_performance_report(
            db,
            athlete_id=1,
        )

    assert result["athlete_id"] == 1

    assert (
        result["fitness_status"]
        == "progressing"
    )

    assert (
        "race_readiness"
        in result
    )

    assert (
        "race_prediction"
        in result
    )


def test_report_contains_prediction():

    db = Mock()

    with patch(
        "api.services.athlete_performance_report_service.generate_coach_insights",
        return_value={
            "status": "progressing",
        },
    ), patch(
        "api.services.athlete_performance_report_service.generate_athlete_training_plan",
        return_value={},
    ):

        result = generate_athlete_performance_report(
            db,
            athlete_id=1,
        )

    assert (
        "predicted_time_seconds"
        in result["race_prediction"]
    )
