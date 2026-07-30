from api.services.ai_coach_conversation_production_bridge_service import (
    build_production_conversation_request,
    execute_ai_coach_brain,
    format_final_conversation_response,
    run_production_conversation_bridge,
)


def test_build_production_request():

    result = build_production_conversation_request(
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

    assert (
        result["athlete_id"]
        == 1
    )

    assert (
        result["question"]
        == "Should I train today?"
    )


def test_execute_ai_coach_brain():

    result = execute_ai_coach_brain(
        request={
            "athlete_id": 1,
            "question": "Train?",
            "athlete_profile": {},
            "training_history": [],
            "recovery_history": [],
            "decision_analysis": {
                "REDUCE_TRAINING": {
                    "success_rate": 90,
                },
            },
            "current_state": {
                "readiness_score": 60,
            },
        },
        ai_response={
            "coach_message": (
                "Recover today."
            ),
        },
    )

    assert (
        result["response"]["strategy"]
        == "RECOVERY_FIRST"
    )


def test_format_final_response():

    result = format_final_conversation_response(
        {
            "response": {
                "personalised_response": {
                    "answer": (
                        "Recovery recommended."
                    ),
                },
                "strategy": (
                    "RECOVERY_FIRST"
                ),
                "confidence": 90,
            }
        }
    )

    assert (
        result["strategy"]
        == "RECOVERY_FIRST"
    )

    assert (
        result["confidence"]
        == 90
    )


def test_full_production_bridge():

    result = run_production_conversation_bridge(
        athlete_id=1,
        question="Should I do intervals?",
        ai_response={
            "coach_message": (
                "Adjust session."
            ),
        },
        athlete_profile={
            "sport": "running",
        },
        training_history=[],
        recovery_history=[],
        decision_analysis={
            "REDUCE_TRAINING": {
                "success_rate": 95,
            },
        },
        current_state={
            "readiness_score": 70,
        },
    )

    assert (
        result["strategy"]
        == "RECOVERY_FIRST"
    )

    assert (
        result["confidence"]
        == 95
    )

    assert (
        "answer"
        in result
    )
