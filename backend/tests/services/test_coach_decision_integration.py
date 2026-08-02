from api.services.coach_decision_integration_service import (
    generate_coach_decision_context,
)


def test_coach_decision_integration_reduces_training():

    athlete_state = {
        "readiness": {
            "score": 50,
        },
        "training": {
            "load_status": "high",
        },
        "performance": {
            "trend": "stable",
        },
    }

    result = generate_coach_decision_context(
        athlete_state,
    )

    assert result["coach_decision"]["decision"] == "REDUCE_TRAINING"

    assert "decision_explanation" in result

    assert "athlete_message" in result["decision_explanation"]


def test_coach_decision_integration_progresses_training():

    athlete_state = {
        "readiness": {
            "score": 90,
        },
        "training": {
            "load_status": "optimal",
        },
        "performance": {
            "trend": "improving",
        },
    }

    result = generate_coach_decision_context(
        athlete_state,
    )

    assert result["coach_decision"]["decision"] == "PROGRESS_TRAINING"


def test_coach_decision_context_contains_state():

    athlete_state = {
        "readiness": {
            "score": 75,
        },
        "training": {
            "load_status": "stable",
        },
        "performance": {
            "trend": "stable",
        },
    }

    result = generate_coach_decision_context(
        athlete_state,
    )

    assert result["athlete_state"] == athlete_state

    assert result["coach_decision"] is not None
