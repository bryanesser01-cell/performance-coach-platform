from api.models.coach_context import CoachContext
from api.services.training_plan_engine import (
    TrainingPlanEngine,
)


def test_builds_recovery_plan():

    context = CoachContext(
        athlete_id=1,
    )

    context.decision = {
        "decision": "RECOVERY_SESSION",
    }

    plan = TrainingPlanEngine().build(
        context,
    )

    assert plan["session_type"] == "Recovery"
    assert plan["duration"] == 40
    assert plan["intensity"] == "Easy"


def test_builds_progress_plan():

    context = CoachContext(
        athlete_id=1,
    )

    context.decision = {
        "decision": "PROGRESS_TRAINING",
    }

    plan = TrainingPlanEngine().build(
        context,
    )

    assert plan["session_type"] == "Workout"
    assert plan["duration"] == 60
    assert plan["intensity"] == "Moderate"


def test_builds_default_plan():

    context = CoachContext(
        athlete_id=1,
    )

    context.decision = {}

    plan = TrainingPlanEngine().build(
        context,
    )

    assert plan["session_type"] == "Easy Run"
    assert plan["duration"] == 45
    assert plan["intensity"] == "Easy"
