from datetime import date, timedelta
import logging

from database.athlete_models import Athlete
from database.goal_models import Goal
from database.training_models import TrainingSession
from schemas.goal import GoalAnalysis

logger = logging.getLogger(__name__)


def analyse_goal(
    goal: Goal,
    athlete: Athlete,
    sessions: list[TrainingSession] | None = None,
) -> GoalAnalysis:
    """
    Analyse a goal using the athlete's recent training history.

    The current implementation provides a simple heuristic that can be
    replaced later by a more sophisticated performance prediction engine.
    """

    logger.info(
        "Analysing goal %s for athlete %s",
        goal.id,
        athlete.id,
    )

    sessions = sessions or []

    if not sessions:
        return GoalAnalysis(
            achievable=False,
            confidence=0.0,
            estimated_completion_date=None,
            message=(
                "No training sessions have been recorded yet. "
                "Complete a few sessions before goal progress can be assessed."
            ),
        )

    recent_sessions = sorted(
        sessions,
        key=lambda s: s.date,
        reverse=True,
    )[:10]

    confidence = min(
        1.0,
        0.3 + (len(recent_sessions) * 0.07),
    )

    achievable = confidence >= 0.6

    if achievable:
        estimated_completion = min(
            goal.target_date,
            date.today() + timedelta(days=30),
        )

        message = (
            "Recent training indicates that this goal appears achievable "
            "if the current training consistency is maintained."
        )
    else:
        estimated_completion = None

        message = (
            "More consistent training data is needed before this goal can "
            "be confidently assessed."
        )

    logger.info("Goal analysis completed successfully.")

    return GoalAnalysis(
        achievable=achievable,
        confidence=round(confidence, 2),
        estimated_completion_date=estimated_completion,
        message=message,
    )
