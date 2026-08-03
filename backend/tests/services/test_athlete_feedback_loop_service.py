from api.models.athlete_digital_twin import (
    AthleteDigitalTwin,
)
from api.services.athlete_feedback_loop_service import (
    AthleteFeedbackLoopService,
)


class FakeSession:
    """
    Fake completed training session.
    """

    id = 1
    session_type = "Threshold Run"
    focus = "5K Development"
    status = "completed"
    notes = "Strong and comfortable session"


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


def test_positive_workout_updates_digital_twin():

    service = AthleteFeedbackLoopService()

    twin = create_test_twin()

    result = service.process_completed_workout(
        twin=twin,
        session=FakeSession(),
    )

    assert (
        result["analysis"]["outcome"]
        == "positive"
    )

    assert (
        result["learning_update"]
        ["performance_update"]["trend"]
        == "improving"
    )

    assert (
        result["digital_twin"]
        .performance_intelligence["trend"]
        == "improving"
    )


def test_positive_workout_updates_recovery_response():

    service = AthleteFeedbackLoopService()

    twin = create_test_twin()

    result = service.process_completed_workout(
        twin=twin,
        session=FakeSession(),
    )

    assert (
        result["digital_twin"]
        .recovery_intelligence["response"]
        == "good"
    )


def test_negative_workout_updates_fatigue_signal():

    service = AthleteFeedbackLoopService()

    twin = create_test_twin()

    class PoorSession:

        id = 2
        session_type = "VO2 Max"
        focus = "Speed"
        status = "completed"
        notes = "Struggled and felt tired"

    result = service.process_completed_workout(
        twin=twin,
        session=PoorSession(),
    )

    assert (
        result["analysis"]["outcome"]
        == "negative"
    )

    assert (
        result["digital_twin"]
        .performance_intelligence["trend"]
        == "declining"
    )
