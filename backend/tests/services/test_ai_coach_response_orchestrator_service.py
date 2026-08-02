from api.services.ai_coach_response_orchestrator_service import (
    build_response_pipeline_context,
    generate_production_ai_coach_answer,
    orchestrate_final_coach_response,
    run_ai_coach_response_orchestrator,
)


def test_build_response_context():

    result = build_response_pipeline_context(
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


def test_orchestrate_final_response():

    result = orchestrate_final_coach_response(
        athlete_id=1,
        ai_response={
            "coach_message": ("Recover today."),
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
                "readiness_score": 60,
            },
        },
    )

    assert result["strategy"] == "RECOVERY_FIRST"


def test_generate_production_answer():

    result = generate_production_ai_coach_answer(
        athlete_id=1,
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
            "readiness_score": 70,
        },
    )

    assert result["confidence"] == 85


def test_full_response_orchestrator():

    result = run_ai_coach_response_orchestrator(
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
            "readiness_score": 50,
        },
    )

    assert result["strategy"] == "RECOVERY_FIRST"

    assert result["confidence"] == 95
