from api.models.athlete_digital_twin import (
    AthleteDigitalTwin,
)
from api.models.coach_context import (
    CoachContext,
)
from api.services.athlete_digital_twin_service import (
    AthleteDigitalTwinService,
)


def test_build_returns_digital_twin():

    service = AthleteDigitalTwinService()

    context = CoachContext(
        athlete_id=1,
    )

    twin = service.build(
        context,
    )

    assert isinstance(
        twin,
        AthleteDigitalTwin,
    )


def test_goal_intelligence_copied():

    service = AthleteDigitalTwinService()

    context = CoachContext(
        athlete_id=1,
    )

    context.goal_intelligence = {
        "goal": "Sub 20 5K",
    }

    twin = service.build(
        context,
    )

    assert (
        twin.goal_intelligence["goal"]
        == "Sub 20 5K"
    )


def test_recovery_intelligence_copied():

    service = AthleteDigitalTwinService()

    context = CoachContext(
        athlete_id=1,
    )

    context.recovery_intelligence = {
        "status": "ready",
    }

    twin = service.build(
        context,
    )

    assert (
        twin.recovery_intelligence["status"]
        == "ready"
    )
