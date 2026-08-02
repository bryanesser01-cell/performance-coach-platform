from api.models.coach_context import CoachContext
from api.services.goal_intelligence_service import (
    GoalIntelligenceService,
)


class GoalIntelligenceStep:
    """
    Analyses athlete goals.
    """

    def __call__(
        self,
        context: CoachContext,
    ) -> None:

        context.goal_intelligence = GoalIntelligenceService().analyse(
            context.athlete_state,
        )
