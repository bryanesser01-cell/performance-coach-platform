from api.models.coach_context import CoachContext
from api.services.coach_brain_service import (
    CoachBrainService,
)
from api.services.workout_recommendation_engine import (
    WorkoutRecommendationEngine,
)


class CoachBrainStep:
    """
    Builds the final coach response.
    """

    def __call__(
        self,
        context: CoachContext,
    ) -> None:

        #
        # Generate recommended workout
        #
        if context.athlete_digital_twin is not None:

            context.training_plan = WorkoutRecommendationEngine().recommend(
                context.athlete_digital_twin,
            )

        #
        # Build final coach response
        #
        CoachBrainService().build_decision(
            context=context,
        )
