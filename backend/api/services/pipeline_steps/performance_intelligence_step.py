from api.models.coach_context import CoachContext
from api.services.performance_intelligence_service import (
    generate_performance_insight,
)


class PerformanceIntelligenceStep:
    """
    Analyses recent athlete performance.
    """

    def __call__(
        self,
        context: CoachContext,
    ) -> None:

        context.performance_intelligence = (
            generate_performance_insight(
                context.athlete_state.get(
                    "training_sessions",
                    [],
                )
            )
        )
