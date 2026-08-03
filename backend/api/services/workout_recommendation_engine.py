"""
Workout Recommendation Engine

Generates candidate workouts,
scores them, and selects the best option.
"""

from api.services.workout_library_service import (
    WorkoutLibraryService,
)
from api.services.workout_scoring_engine import (
    WorkoutScoringEngine,
)


class WorkoutRecommendationEngine:
    """
    Selects the highest scoring workout
    for the athlete.
    """

    def recommend(
        self,
        twin,
    ) -> dict:

        library = WorkoutLibraryService()
        scorer = WorkoutScoringEngine()

        candidates = [
            library.recovery_run(),
            library.easy_run(),
            library.threshold_run(),
            library.tempo_run(),
            library.vo2_max(),
            library.long_run(),
            library.taper_run(),
        ]

        scored_workouts = []

        for workout in candidates:

            result = scorer.score_workout(
                workout=workout,
                twin=twin,
            )

            scored_workouts.append(
                result,
            )

        best_workout = max(
            scored_workouts,
            key=lambda item: item["score"],
        )

        return best_workout
