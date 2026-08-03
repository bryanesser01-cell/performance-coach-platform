from api.models.athlete_digital_twin import AthleteDigitalTwin
from api.models.coach_context import CoachContext


class AthleteDigitalTwinStep:
    """
    Builds the Athlete Digital Twin.
    """

    def __call__(
        self,
        context: CoachContext,
    ) -> None:

        context.athlete_digital_twin = AthleteDigitalTwin(
            athlete=context.athlete_state,
            goal_intelligence=context.goal_intelligence,
            performance_intelligence=context.performance_intelligence,
            recovery_intelligence=context.recovery_intelligence,
            training_load_intelligence=context.training_load_intelligence,
            race_intelligence=context.race_intelligence,
            memory_context=context.memory_context,
            memory_reasoning=context.memory_reasoning,
        )
