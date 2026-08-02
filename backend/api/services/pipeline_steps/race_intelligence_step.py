from api.models.coach_context import CoachContext
from api.services.race_intelligence_service import (
    RaceIntelligenceService,
)


class RaceIntelligenceStep:
    """
    Analyses upcoming race information.
    """

    def __call__(
        self,
        context: CoachContext,
    ) -> None:

        context.race_intelligence = RaceIntelligenceService().analyse(
            context.athlete_state.get(
                "next_race",
            )
        )
