from api.services.ai_coach_live_conversation_service import (
    build_live_conversation_context,
    generate_live_personalised_response,
    process_live_coach_question,
    run_live_ai_coach_pipeline,
)


def test_build_live_context():

    result = build_live_conversation_context(
        athlete_id=1,
        athlete_profile={
            "sport": "running",
        },
        training_history=[],
        recovery_history=[],
        decision_analysis={},
        current_state={},
        question="Should I train today?",
    )

    assert result["athlete_id"] == 1

    assert result["question"] == "Should I train today?"


def test_generate_live_response():

    result = generate_live_personalised_response(
        athlete_id=1,
        ai_response={
            "coach_message": ("Recover today."),
        },
        context={
            "athlete_profile": {},
            "training_history": [],
            "recovery_history": [],
            "decision_analysis": {
                "REDUCE_TRAINING": {
                    "success_rate": 90,
                },
            },
            "current_state": {
                "readiness_score": 50,
            },
        },
    )

    assert result["strategy"] == "RECOVERY_FIRST"

    assert result["confidence"] == 90


def test_process_live_question():

    result = process_live_coach_question(
        athlete_id=1,
        question="Should I train today?",
        ai_response={
            "coach_message": ("Adjust training."),
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
            "readiness_score": 60,
        },
    )

    assert result["athlete_id"] == 1

    assert result["response"]["strategy"] == "RECOVERY_FIRST"


def test_full_live_pipeline():

    result = run_live_ai_coach_pipeline(
        athlete_id=1,
        question="Should I do intervals?",
        ai_response={
            "coach_message": ("Modify session."),
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

    assert result["response"]["confidence"] == 95
