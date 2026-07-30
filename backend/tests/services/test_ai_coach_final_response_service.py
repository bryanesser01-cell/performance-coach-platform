from api.services.ai_coach_final_response_service import (
    build_final_coach_context,
    combine_ai_and_personalised_response,
    generate_final_ai_coach_answer,
    run_final_coach_response_pipeline,
)


def test_build_final_context():

    result = build_final_coach_context(
        athlete_id=1,
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


def test_combine_responses():

    result = combine_ai_and_personalised_response(
        {
            "coach_message": (
                "Train easy."
            ),
        },
        {
            "answer": (
                "Recovery is recommended."
            ),
            "strategy": (
                "RECOVERY_FIRST"
            ),
            "confidence": 90,
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


def test_generate_final_answer():

    result = generate_final_ai_coach_answer(
        athlete_id=1,
        ai_response={
            "coach_message": (
                "Adjust training."
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
            "readiness_score": 70,
        },
    )

    assert (
        result["strategy"]
        == "RECOVERY_FIRST"
    )

    assert (
        result["confidence"]
        == 85
    )


def test_full_final_response_pipeline():

    result = run_final_coach_response_pipeline(
        athlete_id=1,
        ai_response={
            "coach_message": (
                "Recovery day."
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
            "readiness_score": 60,
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
