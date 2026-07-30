from api.services.ai_coach_conversation_final_service import (
    build_final_conversation_context,
    execute_final_ai_coach_path,
    generate_final_conversation_output,
    run_final_conversation_service,
)


def test_build_final_context():

    result = build_final_conversation_context(
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


def test_execute_final_path():

    result = execute_final_ai_coach_path(
        context={
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
        result["strategy"]
        == "RECOVERY_FIRST"
    )

    assert (
        result["confidence"]
        == 90
    )


def test_generate_final_output():

    result = generate_final_conversation_output(
        athlete_id=1,
        question="Should I reduce training?",
        ai_response={
            "coach_message": (
                "Reduce load."
            ),
        },
        athlete_profile={},
        training_history=[],
        recovery_history=[],
        decision_analysis={
            "REDUCE_TRAINING": {
                "success_rate": 85,
            },
        },
        current_state={
            "readiness_score": 50,
        },
    )

    assert (
        result["confidence"]
        == 85
    )


def test_full_final_conversation_service():

    result = run_final_conversation_service(
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
