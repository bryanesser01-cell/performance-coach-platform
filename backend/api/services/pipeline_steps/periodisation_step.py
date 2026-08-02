from api.models.coach_context import CoachContext
from api.services.periodisation_service import (
    PeriodisationEngine,
)


class PeriodisationStep:
    """
    Builds the athlete's periodisation plan.
    """

    def __call__(
        self,
        context: CoachContext,
    ) -> None:

        context.periodisation = PeriodisationEngine().build_plan(
            context.race_intelligence,
        )
