from api.services.ai_coach_pipeline_integration_service import (
    build_production_coach_response,
    integrate_ai_coach_pipeline,
    run_complete_ai_coach_pipeline,
)


def test_integrate_pipeline():

    result = integrate_ai_coach_pipeline(
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
                "success_rate": 90,
            },
        },
        current_state={
            "readiness_score": 60,
        },
    )

    assert result["strategy"] == "RECOVERY_FIRST"

    assert result["confidence"] == 90


def test_build_production_response():

    result = build_production_coach_response(
        {
            "answer": ("Take a recovery day."),
            "strategy": ("RECOVERY_FIRST"),
            "confidence": 85,
        }
    )

    assert result["strategy"] == "RECOVERY_FIRST"

    assert result["confidence"] == 85


def test_complete_pipeline():

    result = run_complete_ai_coach_pipeline(
        athlete_id=1,
        ai_response={
            "coach_message": ("Adjust training."),
        },
        athlete_profile={},
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

    assert result["strategy"] == "RECOVERY_FIRST"

    assert result["confidence"] == 95

    assert "answer" in result
