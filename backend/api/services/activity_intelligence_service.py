def calculate_training_stress(
    activities: list[dict],
) -> int:
    """
    Calculate total training stress
    across a collection of activities.
    """

    return sum(
        activity.get(
            "training_stress",
            0,
        )
        for activity in activities
    )


def calculate_acute_load(
    activities: list[dict],
) -> int:
    """
    Calculate Acute Training Load (ATL).
    """

    return calculate_training_stress(
        activities,
    )


def detect_fitness_trend(
    activities: list[dict],
) -> dict:
    """
    Detect whether fitness is improving,
    stable or declining based on recent
    training stress.
    """

    if len(activities) < 2:
        return {
            "trend": "stable",
        }

    recent = activities[-1].get(
        "training_stress",
        0,
    )

    previous = activities[-2].get(
        "training_stress",
        0,
    )

    if recent > previous:
        trend = "improving"

    elif recent < previous:
        trend = "declining"

    else:
        trend = "stable"

    return {
        "trend": trend,
    }
