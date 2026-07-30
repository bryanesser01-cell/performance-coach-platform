from api.services.ai_coach_personalised_response_service import (
    apply_athlete_strategy,
    build_personalised_response_context,
    generate_final_personalised_answer,
    run_personalised_response_pipeline,
)


def test_build_response_context():

    result = build_personalised_response_context(
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


def test_apply_athlete_strategy():

    result = apply_athlete_strategy(
        coach_response={
            "message": "Recover today.",
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


def test_generate_final_answer():

    result = generate_final_personalised_answer(
        coach_response={
            "message": "Adjust training.",
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
                "readiness_score": 70,
            },
        },
    )

    assert (
        result["confidence"]
        == 85
    )


def test_full_personalised_response_pipeline():

    result = run_personalised_response_pipeline(
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
                "Take a recovery day."
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
