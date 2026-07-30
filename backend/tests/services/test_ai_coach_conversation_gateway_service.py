from api.services.ai_coach_conversation_gateway_service import (
    build_gateway_context,
    generate_gateway_response,
    route_conversation_request,
    run_conversation_gateway,
)


def test_build_gateway_context():

    result = build_gateway_context(
        athlete_id=1,
        athlete_profile={
            "sport": "running",
        },
        training_history=[],
        recovery_history=[],
        decision_analysis={},
        current_state={},
        question="Should I train today?",
    )

    assert (
        result["athlete_id"]
        == 1
    )

    assert (
        result["question"]
        == "Should I train today?"
    )


def test_generate_gateway_response():

    result = generate_gateway_response(
        gateway_context={
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
                "readiness_score": 50,
            },
        },
        ai_response={
            "coach_message": (
                "Recover today."
            ),
        },
    )

    assert (
        result["response"]["strategy"]
        == "RECOVERY_FIRST"
    )


def test_route_conversation_request():

    result = route_conversation_request(
        athlete_id=1,
        question="Should I train?",
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
            "readiness_score": 60,
        },
    )

    assert (
        result["response"]["confidence"]
        == 85
    )


def test_full_gateway_pipeline():

    result = run_conversation_gateway(
        athlete_id=1,
        question="Should I do intervals?",
        ai_response={
            "coach_message": (
                "Modify session."
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
        result["response"]["strategy"]
        == "RECOVERY_FIRST"
    )

    assert (
        result["response"]["confidence"]
        == 95
    )
