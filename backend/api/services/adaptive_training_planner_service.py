"""
Adaptive Training Planner

Coordinates training session generation.
Workout selection is delegated to the
Workout Selection Engine.
"""

from api.services.workout_selection_engine import (
    WorkoutSelectionEngine,
)


class AdaptiveTrainingPlannerService:
    """
    Generates adaptive training sessions
    for an athlete.
    """

    def generate_session(
        self,
        twin,
        decision: str,
    ) -> dict:
        """
        Generate a training session.
        """

        engine = WorkoutSelectionEngine()

        return engine.select_workout(
            twin=twin,
            decision=decision,
        )
