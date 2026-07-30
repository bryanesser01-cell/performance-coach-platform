from api.services.personalised_coach_conversation_service import (
    build_personalised_conversation_context,
    generate_personalised_training_advice,
    merge_strategy_with_coach_response,
    run_personalised_conversation_pipeline,
)


def test_build_personalised_context():

    result = build_personalised_conversation_context(
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
    )

    assert (
        result["athlete_id"]
        == 1
    )

    assert (
        "strategy_context"
        in result
    )


def test_merge_strategy_response():

    result = merge_strategy_with_coach_response(
        {
            "message": (
                "Take an easy day."
            ),
        },
        {
            "strategy_context": {
                "strategy": (
                    "RECOVERY_FIRST"
                ),
                "confidence": 85,
            },
        },
    )

    assert (
        result["personalised_strategy"]
        == "RECOVERY_FIRST"
    )

    assert (
        result["strategy_confidence"]
        == 85
    )


def test_generate_personalised_advice():

    result = generate_personalised_training_advice(
        {
            "personalised_strategy": (
                "RECOVERY_FIRST"
            ),
            "strategy_confidence": 90,
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


def test_full_personalised_pipeline():

    result = run_personalised_conversation_pipeline(
        athlete_id=1,
        athlete_profile={},
        training_history=[],
        recovery_history=[],
        decision_analysis={
            "REDUCE_TRAINING": {
                "success_rate": 95,
            },
        },
        current_state={
            "readiness_score": 80,
        },
        coach_response={
            "message": (
                "Adjusting training."
            ),
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
