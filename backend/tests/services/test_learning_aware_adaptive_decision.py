from api.services.adaptive_coach_decision_service import (
    generate_adaptive_coach_decision,
)
from api.services.coach_learning_memory_service import (
    record_learning_event,
)


def test_adaptive_decision_uses_previous_positive_learning():

    record_learning_event(
        athlete_id=20,
        decision="REDUCE_TRAINING",
        outcome="positive",
        confidence_change=25,
    )

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

    result = generate_adaptive_coach_decision(
        athlete_id=20,
        athlete_state=athlete_state,
    )

    assert (
        result["decision"]
        == "REDUCE_TRAINING"
    )

    assert (
        result["learning_confidence"]
        >= 70
    )


def test_adaptive_decision_returns_learning_context():

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

    result = generate_adaptive_coach_decision(
        athlete_id=21,
        athlete_state=athlete_state,
    )

    assert (
        "learning_confidence"
        in result
    )
