from api.services.ai_coach_production_service import (
    build_production_context,
    generate_production_answer,
    run_production_coach,
)


def test_build_production_context():

    result = build_production_context(
        athlete_id=1,
        athlete_profile={
            "sport": "running",
        },
        training_history=[],
        recovery_history=[],
        decision_analysis={},
        current_state={},
    )

    assert result["athlete_id"] == 1


def test_generate_production_answer():

    result = generate_production_answer(
        athlete_id=1,
        question="Should I train today?",
        ai_response={
            "coach_message": ("Recover today."),
        },
        production_context={
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
    )

    assert result["response"]["strategy"] == "RECOVERY_FIRST"


def test_full_production_coach():

    result = run_production_coach(
        athlete_id=1,
        question=("Should I do intervals?"),
        ai_response={
            "coach_message": ("Adjust training."),
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

    assert result["response"]["strategy"] == "RECOVERY_FIRST"

    assert result["response"]["confidence"] == 95
