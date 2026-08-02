from api.services.ai_coach_live_service_router import (
    build_live_service_request,
    generate_live_service_response,
    route_live_ai_coach_request,
    run_live_service_router,
)


def test_build_live_service_request():

    result = build_live_service_request(
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

    assert result["athlete_id"] == 1

    assert result["question"] == "Should I train today?"


def test_generate_live_service_response():

    result = generate_live_service_response(
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
            "coach_message": ("Recover today."),
        },
    )

    assert result["strategy"] == "RECOVERY_FIRST"

    assert result["confidence"] == 90


def test_route_live_ai_coach_request():

    result = route_live_ai_coach_request(
        athlete_id=1,
        question="Should I reduce training?",
        ai_response={
            "coach_message": ("Reduce load."),
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

    assert result["confidence"] == 85


def test_full_live_router():

    result = run_live_service_router(
        athlete_id=1,
        question="Should I do intervals?",
        ai_response={
            "coach_message": ("Adjust session."),
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

    assert result["strategy"] == "RECOVERY_FIRST"

    assert result["confidence"] == 95
