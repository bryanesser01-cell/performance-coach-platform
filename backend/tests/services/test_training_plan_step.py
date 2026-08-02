from api.models.coach_context import CoachContext
from api.services.pipeline_steps.training_plan_step import (
    TrainingPlanStep,
)


def test_training_plan_step():

    context = CoachContext(
        athlete_id=1,
    )

    context.decision = {
        "decision": "RECOVERY_SESSION",
    }

    TrainingPlanStep()(
        context,
    )

    assert context.training_plan
