from api.models.coach_context import CoachContext
from api.services.training_plan_engine import (
    TrainingPlanEngine,
)


class TrainingPlanStep:
    """
    Builds today's training session.
    """

    def __call__(
        self,
        context: CoachContext,
    ) -> None:

        context.training_plan = TrainingPlanEngine().build(
            context,
        )
