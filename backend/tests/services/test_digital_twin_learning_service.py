from api.services.digital_twin_learning_service import (
    DigitalTwinLearningService,
)


def test_positive_training_outcome_updates_twin():

    service = DigitalTwinLearningService()

    result = service.process_training_outcome(
        outcome={
            "outcome": "positive",
        },
    )

    assert (
        result["performance_update"]["trend"]
        == "improving"
    )

    assert (
        result["training_update"]["training_tolerance"]
        == "increasing"
    )

    assert (
        result["recovery_update"]["response"]
        == "good"
    )


def test_negative_training_outcome_updates_twin():

    service = DigitalTwinLearningService()

    result = service.process_training_outcome(
        outcome={
            "outcome": "negative",
        },
    )

    assert (
        result["performance_update"]["trend"]
        == "declining"
    )

    assert (
        result["training_update"]["training_tolerance"]
        == "decreasing"
    )

    assert (
        result["recovery_update"]["response"]
        == "poor"
    )


def test_neutral_training_outcome_keeps_stability():

    service = DigitalTwinLearningService()

    result = service.process_training_outcome(
        outcome={
            "outcome": "neutral",
        },
    )

    assert (
        result["performance_update"]["trend"]
        == "stable"
    )


def test_missing_outcome_defaults_to_neutral():

    service = DigitalTwinLearningService()

    result = service.process_training_outcome(
        outcome={},
    )

    assert (
        result["performance_update"]["trend"]
        == "stable"
    )
