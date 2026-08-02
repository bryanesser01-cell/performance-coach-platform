from api.services.ai_coach_conversation_orchestrator_service import (
    build_complete_ai_coach_pipeline,
    generate_final_athlete_response,
    orchestrate_coach_conversation,
)


def test_build_complete_pipeline():

    result = build_complete_ai_coach_pipeline(
        athlete_id=1,
        athlete_profile={
            "sport": "running",
        },
        training_history=[],
        recovery_history=[],
        decision_analysis={},
        current_state={},
    )

    assert result["athlete_id"] == 1

    assert "decision_analysis" in result


def test_generate_final_response():

    result = generate_final_athlete_response(
        athlete_id=1,
        ai_response={
            "coach_message": ("Adjust training."),
        },
        pipeline_context={
            "athlete_profile": {},
            "training_history": [],
            "recovery_history": [],
            "decision_analysis": {
                "REDUCE_TRAINING": {
                    "success_rate": 90,
                },
            },
            "current_state": {
                "readiness_score": 70,
            },
        },
    )

    assert result["strategy"] == "RECOVERY_FIRST"

    assert result["confidence"] == 90


def test_full_orchestration_pipeline():

    result = orchestrate_coach_conversation(
        athlete_id=1,
        ai_response={
            "coach_message": ("Recovery recommended."),
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
            "readiness_score": 60,
        },
    )

    assert result["strategy"] == "RECOVERY_FIRST"

    assert result["confidence"] == 95
