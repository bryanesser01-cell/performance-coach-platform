from sqlalchemy.orm import Session

from api.services.athlete_training_plan_service import (
    generate_athlete_training_plan,
)
from api.services.coach_intelligence_service import (
    generate_coach_insights,
)
from api.services.race_prediction_service import (
    predict_race_time,
)
from api.services.race_readiness_service import (
    generate_race_readiness_report,
)


def generate_athlete_performance_report(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Generate complete athlete performance report.

    Combines:
    - Coach intelligence
    - Training plan
    - Race readiness
    - Race prediction
    """

    coach_insights = generate_coach_insights(
        db,
        athlete_id,
    )

    training_plan = generate_athlete_training_plan(
        db,
        athlete_id,
    )

    readiness = generate_race_readiness_report(
        training_load=80,
        performance_score=85,
        fatigue_score=80,
        consistency_score=90,
    )

    prediction = predict_race_time(
        recent_time_seconds=1200,
        readiness_score=readiness[
            "race_readiness_score"
        ],
        performance_trend="improving",
    )

    return {
        "athlete_id": athlete_id,
        "fitness_status": coach_insights.get(
            "status",
            "unknown",
        ),
        "coach_insights": coach_insights,
        "training_plan": training_plan,
        "race_readiness": readiness,
        "race_prediction": prediction,
    }
