from database.models import Activity


def calculate_training_stress(
    duration_seconds: int,
    intensity: str,
) -> int:
    """
    Calculate simple training stress score.

    Future upgrades:
    - Heart rate zones
    - TRIMP
    - Power data
    - Garmin training load
    """

    intensity_multiplier = {
        "easy": 1,
        "moderate": 2,
        "hard": 3,
    }

    multiplier = intensity_multiplier.get(
        intensity.lower(),
        1,
    )

    return int((duration_seconds / 60) * multiplier)


def analyse_activity(
    activity: Activity,
    duration_seconds: int,
    intensity: str = "moderate",
) -> dict:
    """
    Analyse completed athlete activity.

    Returns:
    - Training stress
    - Activity category
    - Performance insight
    """

    stress = calculate_training_stress(
        duration_seconds=duration_seconds,
        intensity=intensity,
    )

    if stress >= 150:
        recommendation = "High training stress. " "Prioritise recovery."

    elif stress >= 75:
        recommendation = "Productive training session. " "Monitor recovery."

    else:
        recommendation = "Low stress session. " "Suitable for building consistency."

    return {
        "activity_id": activity.id,
        "athlete_id": activity.athlete_id,
        "category": activity.category,
        "name": activity.name,
        "training_stress": stress,
        "recommendation": recommendation,
    }


def detect_fitness_trend(
    activities: list[dict],
) -> dict:
    """
    Detect simple fitness trend.

    Future:
    - Pace improvement
    - VO2 max
    - Race prediction
    - Chronic load
    """

    if len(activities) < 2:
        trend = "insufficient_data"

    else:
        first = activities[0]["training_stress"]
        last = activities[-1]["training_stress"]

        if last > first:
            trend = "improving"

        elif last < first:
            trend = "declining"

        else:
            trend = "stable"

    return {
        "trend": trend,
        "activity_count": len(activities),
    }


def generate_activity_learning_event(
    analysis: dict,
) -> dict:
    """
    Convert activity analysis into
    AI Coach learning signal.
    """

    stress = analysis["training_stress"]

    if stress > 150:
        outcome = "high_load"

    elif stress < 50:
        outcome = "low_load"

    else:
        outcome = "productive"

    return {
        "activity_id": analysis["activity_id"],
        "outcome": outcome,
        "training_stress": stress,
    }
