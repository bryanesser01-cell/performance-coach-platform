from api.models.athlete_digital_twin import (
    AthleteDigitalTwin,
)
from api.services.digital_twin_update_service import (
    DigitalTwinUpdateService,
)


def create_test_twin():

    return AthleteDigitalTwin(
        performance_intelligence={
            "trend": "stable",
        },
        recovery_intelligence={
            "response": "unknown",
        },
        training_load_intelligence={
            "training_tolerance": "stable",
        },
    )


def test_positive_learning_updates_performance():

    service = DigitalTwinUpdateService()

    twin = create_test_twin()

    result = service.apply_learning_update(
        twin=twin,
        learning_update={
            "performance_update": {
                "trend": "improving",
            },
            "recovery_update": {
                "response": "good",
            },
            "training_update": {
                "training_tolerance": "increasing",
            },
        },
    )

    assert (
        result.performance_intelligence["trend"]
        == "improving"
    )


def test_positive_learning_updates_recovery():

    service = DigitalTwinUpdateService()

    twin = create_test_twin()

    result = service.apply_learning_update(
        twin=twin,
        learning_update={
            "recovery_update": {
                "response": "good",
            },
        },
    )

    assert (
        result.recovery_intelligence["response"]
        == "good"
    )


def test_learning_updates_training_tolerance():

    service = DigitalTwinUpdateService()

    twin = create_test_twin()

    result = service.apply_learning_update(
        twin=twin,
        learning_update={
            "training_update": {
                "training_tolerance": "increasing",
            },
        },
    )

    assert (
        result.training_load_intelligence[
            "training_tolerance"
        ]
        == "increasing"
    )


def test_empty_learning_update_does_not_break():

    service = DigitalTwinUpdateService()

    twin = create_test_twin()

    result = service.apply_learning_update(
        twin=twin,
        learning_update={},
    )

    assert result is twin
