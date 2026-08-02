from api.models.coach_context import CoachContext
from api.services.training_load_intelligence_service import (
    TrainingLoadIntelligenceService,
)


class TrainingLoadIntelligenceStep:
    """
    Analyses athlete training load.
    """

    def __call__(
        self,
        context: CoachContext,
    ) -> None:

        context.training_load_intelligence = TrainingLoadIntelligenceService().analyse(
            context.athlete_state.get(
                "training_sessions",
                [],
            )
        )
