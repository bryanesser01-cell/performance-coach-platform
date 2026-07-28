from sqlalchemy.orm import Session

from api.services.coach_recommendation_service import (
    generate_recommendation,
)
from api.services.goal_analysis import analyse_goal
from api.services.performance_engine import analyse_training
from api.services.performance_trend_service import (
    generate_athlete_performance_trends,
)
from database.repositories.activity_metric_repository import (
    ActivityMetricRepository,
)
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
    - Performance trends
    """

    training_repository = TrainingRepository(
        db,
    )

    goal_repository = GoalRepository(
        db,
    )

    athlete_repository = AthleteRepository(
        db,
    )

    activity_metric_repository = ActivityMetricRepository(
        db,
    )

    sessions = training_repository.get_recent_sessions(
        athlete_id,
    )

    athlete = athlete_repository.get_by_id(
        athlete_id,
    )

    goals = goal_repository.get_active_goals(
        athlete_id,
    )

    trends = generate_athlete_performance_trends(
        athlete_id,
        activity_metric_repository,
    )

    if not sessions:
        return {
            "athlete_id": athlete_id,
            "status": "insufficient_data",
            "goals": [],
            "performance_trends": trends,
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
            "performance_trends": trends,
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
    # Training Recommendations
    # -----------------------------

    recommendations.extend(
        analysis.recommendations,
    )

    # -----------------------------
    # Performance Trend Intelligence
    # -----------------------------

    if trends["pace_trend"] == "improving":
        insights.append(
            "Running pace is improving over recent activities.",
        )

    if trends["distance_trend"] == "increasing":
        recommendations.append(
            "Continue progressive distance increases while monitoring recovery.",
        )

    if trends["training_load_trend"] == "increasing":
        insights.append(
            "Training load is increasing. Monitor fatigue and recovery.",
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

        # -----------------------------
# Coach Recommendation
# -----------------------------

    recommendation = generate_recommendation(
    status=status,
    pace_trend=trends["pace_trend"],
    training_load_trend=trends["training_load_trend"],
)

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
    "performance_trends": trends,
    "goals": goal_insights,
    "insights": insights,
    "recommendations": recommendations,
    "coach_recommendation": recommendation,
}
