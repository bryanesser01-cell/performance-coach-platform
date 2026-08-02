from api.services.coach_decision_integration_service import (
    generate_coach_decision_context,
)


def test_ai_coach_adaptive_integration_explains_reduced_training():

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

    decision = result["coach_decision"]

    explanation = result["decision_explanation"]

    assert decision["decision"] == "REDUCE_TRAINING"

    assert explanation is not None

    assert "athlete_message" in explanation


def test_ai_coach_adaptive_integration_explains_progression():

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

    decision = result["coach_decision"]

    assert decision["decision"] == "PROGRESS_TRAINING"


def test_ai_coach_adaptive_context_contains_athlete_state():

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

    assert result["decision_explanation"] is not None
