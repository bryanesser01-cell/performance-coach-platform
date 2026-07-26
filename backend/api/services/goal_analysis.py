import logging
from typing import Any

from api.services.performance_engine import analyse_training
from api.services.recommendation_engine import generate_recommendations
from schemas.athlete import AthleteResponse
from schemas.goal import GoalResponse
from schemas.training import TrainingSessionResponse

logger = logging.getLogger(__name__)


def analyse_goal(
    goal: GoalResponse,
    athlete: AthleteResponse,
    sessions: list[TrainingSessionResponse] | None = None,
) -> dict[str, Any]:
    """
    Analyse an athlete's goal and return progress, status,
    priority and coaching recommendations.
    """

    logger.info(
        "Analysing goal '%s' for athlete ID %s.",
        goal.goal_type,
        athlete.id,
    )

    recommendations: list[Any] = []

    # Generate recommendations from training history
    if sessions:
        analysis = analyse_training(sessions)

        if analysis is not None:
            recommendations = generate_recommendations(
                analysis
            )

    # Calculate progress safely
    if goal.target_value <= 0:
        progress = 0.0
    else:
        progress = (
            goal.current_value / goal.target_value
        ) * 100

    # Keep progress within sensible limits
    progress = max(0.0, min(progress, 100.0))

    # Remaining amount to reach target
    remaining = max(
        goal.target_value - goal.current_value,
        0.0,
    )

    # Goal status
    if progress >= 100:
        status = "Completed"
    elif progress >= 95:
        status = "Almost There"
    elif progress >= 80:
        status = "On Track"
    elif progress >= 60:
        status = "Behind"
    else:
        status = "Needs Improvement"

    # Priority
    if remaining <= 1:
        priority = "Critical"
    elif remaining <= 3:
        priority = "High"
    elif remaining <= 5:
        priority = "Medium"
    else:
        priority = "Low"

    logger.info(
        "Goal analysis completed successfully."
    )

    return {
        "progress_percent": round(progress, 1),
        "remaining": round(remaining, 1),
        "remaining_unit": goal.target_unit,
        "status": status,
        "priority": priority,
        "recommendations": recommendations,
    }
