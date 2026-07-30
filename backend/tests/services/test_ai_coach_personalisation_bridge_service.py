from api.services.ai_coach_personalisation_bridge_service import (
    apply_personalised_strategy,
    build_full_personalised_coach_context,
    generate_final_coach_response,
    run_ai_coach_personalisation_bridge,
)


def test_build_full_context():

    result = build_full_personalised_coach_context(
        athlete_id=1,
        athlete_profile={
            "sport": "running",
        },
        training_history=[],
        recovery_history=[],
        decision_analysis={},
        current_state={
            "readiness_score": 80,
        },
    )

    assert (
        result["athlete_id"]
        == 1
    )

    assert (
        "decision_analysis"
        in result
    )


def test_apply_personalised_strategy():

    result = apply_personalised_strategy(
        coach_response={
            "message": (
                "Adjust training."
            ),
        },
        personalised_context={
            "athlete_id": 1,
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

    assert (
        result["strategy"]
        == "RECOVERY_FIRST"
    )


def test_generate_final_response():

    result = generate_final_coach_response(
        coach_response={
            "message": "Train easy.",
        },
        personalised_context={
            "athlete_id": 1,
            "athlete_profile": {},
            "training_history": [],
            "recovery_history": [],
            "decision_analysis": {
                "REDUCE_TRAINING": {
                    "success_rate": 85,
                },
            },
            "current_state": {
                "readiness_score": 60,
            },
        },
    )

    assert (
        result["confidence"]
        == 85
    )


def test_full_personalisation_bridge():

    result = run_ai_coach_personalisation_bridge(
        athlete_id=1,
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
            "readiness_score": 75,
        },
        coach_response={
            "message": (
                "Recovery recommended."
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
