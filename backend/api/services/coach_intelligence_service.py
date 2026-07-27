from sqlalchemy.orm import Session

from api.services.performance_engine import analyse_training
from database.repositories.training_repository import TrainingRepository


def generate_coach_insights(
    db: Session,
    athlete_id: int,
):
    """
    Generate coaching insights for an athlete.

    Combines training history analysis with coaching
    recommendations.
    """

    repository = TrainingRepository(db)

    sessions = repository.get_recent_sessions(
        athlete_id,
    )

    if not sessions:
        return {
            "athlete_id": athlete_id,
            "status": "insufficient_data",
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
        "insights": insights,
        "recommendations": recommendations,
    }
