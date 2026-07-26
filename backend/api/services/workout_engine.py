import logging

from api.services.workout_rules import recommend_from_rules
from schemas.analysis import PerformanceAnalysis
from schemas.workout import WorkoutRecommendation

logger = logging.getLogger(__name__)


def recommend_workout(
    analysis: PerformanceAnalysis,
) -> WorkoutRecommendation:
    """
    Generate the next recommended workout based on the
    athlete's performance analysis.
    """

    logger.info("Generating workout recommendation.")

    workout = recommend_from_rules(analysis)

    logger.info(
        "Workout recommendation generated successfully."
    )

    return workout
