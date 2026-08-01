from api.models.coach_context import CoachContext
from api.services.recovery_intelligence_service import (
    generate_recovery_recommendation,
)


class RecoveryIntelligenceStep:
    """
    Builds recovery intelligence.
    """

    def __call__(
        self,
        context: CoachContext,
    ) -> None:

        readiness = (
            context.athlete_state
            .get(
                "readiness",
                {},
            )
            .get(
                "score",
                0,
            )
        )

        context.recovery_intelligence = (
            generate_recovery_recommendation(
                readiness,
            )
        )
