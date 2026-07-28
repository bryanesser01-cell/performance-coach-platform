from sqlalchemy.orm import Session

from api.services.coach_intelligence_service import (
    generate_coach_insights,
)
from api.services.training_plan_service import (
    generate_training_plan,
)


def generate_athlete_training_plan(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Generate a personalised training plan for an athlete.

    Uses:
    - Coach intelligence insights
    - Performance trends
    - Recommendations
    """

    coach_insights = generate_coach_insights(
        db,
        athlete_id,
    )

    status = coach_insights.get(
        "status",
        "progressing",
    )

    trends = coach_insights.get(
        "performance_trends",
        {},
    )

    recommendation = coach_insights.get(
        "coach_recommendation",
        {},
    )

    goal = "5k"

    plan = generate_training_plan(
        goal=goal,
        fitness_status=status,
        training_load=trends.get(
            "training_load_trend",
            "stable",
        ),
    )

    return {
        "athlete_id": athlete_id,
        "goal": goal,
        "coach_recommendation": recommendation,
        "training_plan": plan,
    }
