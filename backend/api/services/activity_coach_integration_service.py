from api.services.activity_intelligence_service import (
    detect_fitness_trend,
)


def build_activity_coach_context(
    activities: list[dict],
) -> dict:
    """
    Build AI Coach context from activity history.

    Uses:
    - Training stress
    - Fitness trend
    - Activity count
    """

    total_stress = sum(
        activity.get(
            "training_stress",
            0,
        )
        for activity in activities
    )

    trend = detect_fitness_trend(
        activities,
    )

    return {
        "activity_count": len(activities),
        "total_training_stress": total_stress,
        "fitness_trend": trend["trend"],
    }


def detect_training_risk(
    activity_context: dict,
) -> dict:
    """
    Detect excessive training load risk.
    """

    stress = activity_context.get(
        "total_training_stress",
        0,
    )

    if stress >= 500:
        risk = "high"

        message = (
            "Training load is high. "
            "Recovery should be prioritised."
        )

    elif stress >= 250:
        risk = "moderate"

        message = (
            "Training load is increasing. "
            "Monitor fatigue."
        )

    else:
        risk = "low"

        message = (
            "Training load is manageable."
        )

    return {
        "risk": risk,
        "message": message,
    }


def generate_activity_based_recommendation(
    activity_context: dict,
) -> dict:
    """
    Generate AI Coach recommendation
    based on recent activities.
    """

    risk = detect_training_risk(
        activity_context,
    )

    trend = activity_context.get(
        "fitness_trend",
        "unknown",
    )

    if risk["risk"] == "high":

        recommendation = (
            "Schedule recovery before "
            "the next hard session."
        )

    elif trend == "improving":

        recommendation = (
            "Fitness is improving. "
            "Continue progressive training."
        )

    elif trend == "declining":

        recommendation = (
            "Reduce load and rebuild consistency."
        )

    else:

        recommendation = (
            "Maintain current training approach."
        )

    return {
        "fitness_trend": trend,
        "training_risk": risk["risk"],
        "recommendation": recommendation,
    }
