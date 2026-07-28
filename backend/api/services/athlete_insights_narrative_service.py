def generate_insight_narrative(
    fitness_trend: str,
    pace_improvement_seconds_per_km: float,
    consistency_score: int,
    training_load_status: str = "stable",
) -> dict:
    """
    Generate athlete-friendly coaching narrative.
    """

    insights = []

    if fitness_trend == "improving":
        insights.append(
            "Your fitness is improving based on your recent training history."
        )

    elif fitness_trend == "declining":
        insights.append(
            "Your recent performance suggests you may need additional recovery."
        )

    else:
        insights.append(
            "Your performance has remained consistent."
        )

    if pace_improvement_seconds_per_km > 0:
        insights.append(
            (
                "Your pace has improved by "
                f"{pace_improvement_seconds_per_km}"
                " seconds per kilometre."
            )
        )

    if consistency_score >= 80:
        insights.append(
            "Your training consistency is excellent."
        )

    elif consistency_score >= 50:
        insights.append(
            "Your training consistency is building."
        )

    else:
        insights.append(
            "Focus on maintaining regular training habits."
        )

    if training_load_status == "high":
        recommendation = (
            "Consider recovery to absorb your training gains."
        )
    else:
        recommendation = (
            "Continue your current progression."
        )

    return {
        "summary": " ".join(insights),
        "insights": insights,
        "recommendation": recommendation,
    }
