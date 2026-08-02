from api.services.athlete_strategy_integration_service import (
    apply_strategy_to_decision,
    build_personalised_coach_context,
    generate_personalised_coach_response,
    run_personalised_strategy_pipeline,
)


def test_build_personalised_context():

    result = build_personalised_coach_context(
        athlete_id=1,
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
            "readiness_score": 50,
        },
    )

    assert result["athlete_id"] == 1

    assert "personalised_strategy" in result


def test_apply_strategy_to_decision():

    result = apply_strategy_to_decision(
        {
            "decision": "PROGRESS_TRAINING",
        },
        {
            "personalised_strategy": {
                "recommended_strategy": ("RECOVERY_FIRST"),
                "confidence": 85,
            }
        },
    )

    assert result["athlete_strategy"] == "RECOVERY_FIRST"

    assert result["strategy_confidence"] == 85


def test_generate_personalised_response():

    result = generate_personalised_coach_response(
        {
            "decision": "REDUCE_TRAINING",
            "athlete_strategy": ("RECOVERY_FIRST"),
            "strategy_confidence": 90,
        }
    )

    assert result["strategy"] == "RECOVERY_FIRST"

    assert result["confidence"] == 90


def test_full_personalised_strategy_pipeline():

    result = run_personalised_strategy_pipeline(
        athlete_id=1,
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
            "readiness_score": 70,
        },
        decision={
            "decision": "PROGRESS_TRAINING",
        },
    )

    assert result["strategy"] == "RECOVERY_FIRST"

    assert result["confidence"] == 90
