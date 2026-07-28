from sqlalchemy.orm import Session

from api.services.athlete_insights_narrative_service import (
    generate_insight_narrative,
)
from api.services.athlete_performance_report_service import (
    generate_athlete_performance_report,
)


def generate_ai_coach_response(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Generate unified AI coach response.

    Combines:
    - Performance report
    - Coaching insights
    - Training guidance
    - Narrative explanation
    """

    report = generate_athlete_performance_report(
        db,
        athlete_id,
    )

    coach_insights = report.get(
        "coach_insights",
        {},
    )

    race_readiness = report.get(
        "race_readiness",
        {},
    )

    race_prediction = report.get(
        "race_prediction",
        {},
    )

    narrative = generate_insight_narrative(
        fitness_trend=report.get(
            "fitness_status",
            "unknown",
        ),
        pace_improvement_seconds_per_km=0,
        consistency_score=80,
    )

    return {
        "athlete_id": athlete_id,
        "athlete_status": report.get(
            "fitness_status",
            "unknown",
        ),
        "coach_insights": coach_insights,
        "race_readiness": race_readiness,
        "race_prediction": race_prediction,
        "coach_message": narrative[
            "summary"
        ],
        "recommendation": narrative[
            "recommendation"
        ],
    }
