from api.services.ai_coach_conversation_adapter_service import (
    adapt_conversation_request,
    convert_ai_response_to_gateway,
    run_adapted_conversation,
)


def test_adapt_conversation_request():

    result = adapt_conversation_request(
        athlete_id=1,
        question="Should I train today?",
        athlete_profile={
            "sport": "running",
        },
        training_history=[],
        recovery_history=[],
        decision_analysis={},
        current_state={},
    )

    assert result["athlete_id"] == 1

    assert result["question"] == "Should I train today?"


def test_convert_ai_response():

    result = convert_ai_response_to_gateway(
        {
            "coach_message": ("Recover today."),
        }
    )

    assert result["coach_message"] == "Recover today."


def test_run_adapted_conversation():

    result = run_adapted_conversation(
        athlete_id=1,
        question="Should I reduce training?",
        ai_response={
            "coach_message": ("Reduce load."),
        },
        athlete_profile={
            "sport": "running",
        },
        training_history=[],
        recovery_history=[],
        decision_analysis={
            "REDUCE_TRAINING": {
                "success_rate": 90,
            },
        },
        current_state={
            "readiness_score": 60,
        },
    )

    assert result["response"]["strategy"] == "RECOVERY_FIRST"

    assert result["response"]["confidence"] == 90
