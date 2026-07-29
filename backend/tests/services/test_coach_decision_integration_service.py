from api.services.coach_decision_integration_service import (
    build_coach_decision_context,
    generate_coach_decision,
)


def test_high_readiness_improving_athlete_progresses():

    athlete_state = {
        "readiness": {
            "score": 85,
        },
        "training": {
            "load_status": "optimal",
        },
        "performance": {
            "trend": "improving",
        },
    }

    result = generate_coach_decision(
        athlete_state,
    )

    assert (
        result["decision"]
        == "progress_training"
    )


def test_low_readiness_requires_recovery():

    athlete_state = {
        "readiness": {
            "score": 45,
        },
        "training": {
            "load_status": "optimal",
        },
        "performance": {
            "trend": "stable",
        },
    }

    result = generate_coach_decision(
        athlete_state,
    )

    assert (
        result["decision"]
        == "recover"
    )


def test_high_training_load_reduces_intensity():

    athlete_state = {
        "readiness": {
            "score": 75,
        },
        "training": {
            "load_status": "high",
        },
        "performance": {
            "trend": "stable",
        },
    }

    result = generate_coach_decision(
        athlete_state,
    )

    assert (
        result["decision"]
        == "reduce_load"
    )


def test_build_coach_decision_context():

    athlete_state = {
        "readiness": {
            "score": 85,
        },
        "training": {
            "load_status": "optimal",
        },
        "performance": {
            "trend": "improving",
        },
    }

    context = build_coach_decision_context(
        athlete_state,
    )

    assert (
        "coach_decision"
        in context
    )
