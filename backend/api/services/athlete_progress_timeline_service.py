def calculate_progress_trend(
    activities: list[dict],
) -> str:
    """
    Determine athlete progress trend.
    """

    if len(activities) < 2:
        return "insufficient_data"

    first = activities[0]
    last = activities[-1]

    if last["pace"] < first["pace"]:
        return "improving"

    if last["pace"] > first["pace"]:
        return "declining"

    return "stable"


def calculate_pace_improvement(
    activities: list[dict],
) -> float:
    """
    Calculate pace improvement in seconds per km.
    """

    if len(activities) < 2:
        return 0.0

    first_pace = activities[0]["pace"]
    last_pace = activities[-1]["pace"]

    return round(
        first_pace - last_pace,
        2,
    )


def calculate_consistency_score(
    activities: list[dict],
) -> int:
    """
    Calculate training consistency score.
    """

    if not activities:
        return 0

    score = len(activities) * 10

    return min(
        score,
        100,
    )


def generate_progress_timeline(
    activities: list[dict],
) -> dict:
    """
    Generate athlete progress timeline.
    """

    return {
        "period": "12_weeks",
        "fitness_trend": calculate_progress_trend(
            activities,
        ),
        "pace_improvement_seconds_per_km": (
            calculate_pace_improvement(
                activities,
            )
        ),
        "consistency_score": calculate_consistency_score(
            activities,
        ),
        "milestones": [
            "Training history analysed.",
        ],
    }
