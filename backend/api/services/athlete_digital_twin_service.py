"""
Athlete Digital Twin Service

Builds a complete digital representation
of an athlete for the AI Coach.
"""

from api.models.athlete_digital_twin import (
    AthleteDigitalTwin,
)
from api.models.coach_context import (
    CoachContext,
)


class AthleteDigitalTwinService:
    """
    Builds the Athlete Digital Twin.

    Future versions will enrich this object
    with learning, predictions and adaptive
    coaching insights.
    """

    def build(
        self,
        context: CoachContext,
    ) -> AthleteDigitalTwin:
        """
        Build the Athlete Digital Twin
        from the current CoachContext.
        """

        return AthleteDigitalTwin(
            athlete=context.athlete_state,
            goal_intelligence=context.goal_intelligence,
            performance_intelligence=(context.performance_intelligence),
            recovery_intelligence=(context.recovery_intelligence),
            training_load_intelligence=(context.training_load_intelligence),
            race_intelligence=(context.race_intelligence),
            memory_context=(context.memory_context),
            memory_reasoning=(context.memory_reasoning),
        )
