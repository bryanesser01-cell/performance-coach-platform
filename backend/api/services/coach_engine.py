import logging

from core.exceptions import InvalidTrainingDataError

from schemas.coach import CoachResponse
from schemas.training import TrainingSessionResponse

from api.services.performance_engine import analyse_training
from api.services.workout_engine import recommend_workout
from api.services.recommendation_engine import (
    generate_recommendations,
)

logger = logging.getLogger(__name__)


def generate_coach_response(
    sessions: list[TrainingSessionResponse],
) -> CoachResponse:
    """
    Generate a complete coaching response including
    performance analysis, workout recommendation and
    coaching recommendations.
    """

    logger.info("Generating coach response.")

    analysis = analyse_training(sessions)

    if analysis is None:
        logger.warning("No training sessions supplied for analysis.")

        raise InvalidTrainingDataError("No training sessions found for analysis.")

    workout = recommend_workout(analysis)

    recommendations = generate_recommendations(analysis)

    logger.info("Coach response generated successfully.")

    return CoachResponse(
        analysis=analysis,
        workout=workout,
        recommendations=recommendations,
    )
