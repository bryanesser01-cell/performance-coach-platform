from api.services.coach_learning_service import (
    analyse_training_session_response,
    build_learning_loop_result,
    identify_training_patterns,
)


def test_positive_training_response():

    result = analyse_training_session_response(
        {
            "session_type": "intervals",
            "athlete_feedback": "strong",
            "date": "2026-07-30",
        }
    )

    assert result["response"] == "POSITIVE"


def test_identify_training_patterns():

    result = identify_training_patterns(
        [
            {
                "session_type": "tempo",
                "athlete_feedback": "good",
            },
            {
                "session_type": "long_run",
                "athlete_feedback": "tired",
            },
        ]
    )

    assert "tempo" in result["responds_well_to"]

    assert "long_run" in result["struggles_with"]


def test_learning_loop():

    result = build_learning_loop_result(
        athlete_profile={
            "name": "Athlete",
            "event": "1500m",
        },
        sessions=[
            {
                "session_type": "intervals",
                "athlete_feedback": "good",
            }
        ],
    )

    assert result["ready_for_future_training"] is True
