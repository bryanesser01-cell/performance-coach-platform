from sqlalchemy.orm import Session

from api.services.goal_analysis import analyse_goal
from api.services.performance_engine import analyse_training
from database.repositories.athlete_repository import AthleteRepository
from database.repositories.goal_repository import GoalRepository
from database.repositories.training_repository import TrainingRepository


def generate_coach_insights(
    db: Session,
    athlete_id: int,
):
    """
    Generate coaching insights for an athlete.

    Combines:
    - Training performance analysis
    - Athlete goals
    - Goal progress analysis
    """

    training_repository = TrainingRepository(db)
    goal_repository = GoalRepository(db)
    athlete_repository = AthleteRepository(db)

    sessions = training_repository.get_recent_sessions(
        athlete_id,
    )

    athlete = athlete_repository.get_by_id(
        athlete_id,
    )

    goals = goal_repository.get_active_goals(
        athlete_id,
    )

    if not sessions:
        return {
            "athlete_id": athlete_id,
            "status": "insufficient_data",
            "goals": [],
            "insights": [
                "Not enough training data available.",
            ],
            "recommendations": [
                "Complete more training sessions to generate insights.",
            ],
        }

    analysis = analyse_training(
        sessions,
    )

    if analysis is None:
        return {
            "athlete_id": athlete_id,
            "status": "insufficient_data",
            "goals": [],
            "insights": [],
            "recommendations": [],
        }

    insights = []
    recommendations = []

    # -----------------------------
    # Training Risks
    # -----------------------------

    if analysis.risks:
        insights.extend(
            analysis.risks,
        )

    # -----------------------------
    # Training Strengths
    # -----------------------------

    if analysis.strengths:
        insights.extend(
            analysis.strengths,
        )

    # -----------------------------
    # Recommendations
    # -----------------------------

    recommendations.extend(
        analysis.recommendations,
    )

    # -----------------------------
    # Goal Intelligence
    # -----------------------------

    goal_insights = []

    if athlete:
        for goal in goals:
            goal_insights.append(
                {
                    "goal_type": goal.goal_type,
                    "target_value": goal.target_value,
                    "current_value": goal.current_value,
                    "analysis": analyse_goal(
                        goal,
                        athlete,
                        sessions,
                    ),
                }
            )

    # -----------------------------
    # Overall Status
    # -----------------------------

    if len(analysis.risks) == 0:
        status = "progressing"
    else:
        status = "needs_attention"

    return {
        "athlete_id": athlete_id,
        "status": status,
        "metrics": {
            "total_sessions": analysis.total_sessions,
            "total_distance": analysis.total_distance,
            "training_load": analysis.total_training_load,
            "average_pace": analysis.average_pace,
            "average_heart_rate": analysis.average_heart_rate,
            "longest_run": analysis.longest_run,
        },
        "goals": goal_insights,
        "insights": insights,
        "recommendations": recommendations,
    }
