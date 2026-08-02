from api.services.coach_learning_memory_service import (
    record_learning_event,
)
from api.services.learning_aware_decision_service import (
    build_learning_aware_context,
    generate_learning_aware_decision,
)


def test_learning_aware_decision_uses_positive_history():

    record_learning_event(
        athlete_id=10,
        decision="REDUCE_TRAINING",
        outcome="positive",
        confidence_change=25,
    )

    result = generate_learning_aware_decision(
        athlete_id=10,
        proposed_decision="REDUCE_TRAINING",
    )

    assert result["recommended_decision"] == "REDUCE_TRAINING"

    assert result["confidence"] == 75


def test_learning_aware_decision_detects_low_confidence():

    record_learning_event(
        athlete_id=11,
        decision="PROGRESS_TRAINING",
        outcome="negative",
        confidence_change=-20,
    )

    result = generate_learning_aware_decision(
        athlete_id=11,
        proposed_decision="PROGRESS_TRAINING",
    )

    assert result["confidence"] == 30

    assert "reviewing" in result["reason"]


def test_learning_context_contains_decision():

    result = build_learning_aware_context(
        athlete_id=12,
        decision="REDUCE_TRAINING",
    )

    assert (
        result["learning_aware_decision"]["recommended_decision"] == "REDUCE_TRAINING"
    )
