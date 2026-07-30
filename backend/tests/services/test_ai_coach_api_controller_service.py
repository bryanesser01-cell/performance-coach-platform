from api.services.ai_coach_api_controller_service import (
    execute_api_coach_request,
    generate_api_coach_response,
    prepare_api_coach_request,
    run_api_coach_controller,
)


def test_prepare_api_request():

    result = prepare_api_coach_request(
        athlete_id=1,
        question="Should I train today?",
        ai_response={
            "coach_message": "Recover today.",
        },
        athlete_profile={
            "sport": "running",
        },
        training_history=[],
        recovery_history=[],
        decision_analysis={},
        current_state={},
    )

    assert result["athlete_id"] == 1

    assert (
        result["question"]
        == "Should I train today?"
    )


def test_execute_api_request():

    result = execute_api_coach_request(
        {
            "athlete_id": 1,
            "question": "Train?",
            "ai_response": {
                "coach_message": "Recover today.",
            },
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


def test_generate_api_response():

    result = generate_api_coach_response(
        athlete_id=1,
        question="Should I reduce training?",
        ai_response={
            "coach_message": "Reduce load.",
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


def test_full_api_controller():

    result = run_api_coach_controller(
        athlete_id=1,
        question="Should I do intervals?",
        ai_response={
            "coach_message": "Adjust session.",
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
