from api.services.ai_coach_production_controller_service import (
    build_controller_request,
    execute_production_controller,
    generate_controller_response,
    run_production_controller,
)


def test_build_controller_request():

    result = build_controller_request(
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

    assert (
        result["question"]
        == "Should I train today?"
    )


def test_execute_production_controller():

    result = execute_production_controller(
        request={
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


def test_generate_controller_response():

    result = generate_controller_response(
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


def test_full_production_controller():

    result = run_production_controller(
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
