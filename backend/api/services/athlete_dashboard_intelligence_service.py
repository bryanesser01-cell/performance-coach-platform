"""
Athlete Dashboard Intelligence Service

Combines all dashboard intelligence
into one athlete performance profile.

Combines:
- fitness
- training status
- race readiness
- prediction
- scorecard
- coaching insight
"""


from api.services.dashboard_insight_service import (
    generate_dashboard_insight,
)
from api.services.performance_scorecard_service import (
    generate_performance_scorecard,
)


def generate_dashboard_intelligence(
    fitness_summary: dict,
    training_status: dict,
    race_readiness: dict,
    prediction: dict,
    timeline: dict,
    limitation: dict,
) -> dict:
    """
    Generate complete athlete intelligence profile.
    """


    scorecard = generate_performance_scorecard(
        fitness_score=fitness_summary.get(
            "fitness_score",
            0,
        ),

        consistency_score=training_status.get(
            "consistency_score",
            0,
        ),

        readiness_score=race_readiness.get(
            "readiness_score",
            0,
        ),

        improvement_score=fitness_summary.get(
            "improvement_score",
            0,
        ),

        trend=fitness_summary.get(
            "trend",
            "unknown",
        ),
    )


    insight = generate_dashboard_insight(
        scorecard,

        timeline,

        limitation,
    )


    return {

        "fitness_summary": fitness_summary,

        "training_status": training_status,

        "race_readiness": race_readiness,

        "prediction": prediction,

        "scorecard": scorecard,

        "insight": insight,
    }
