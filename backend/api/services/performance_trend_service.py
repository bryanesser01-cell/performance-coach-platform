from database.repositories.activity_metric_repository import (
    ActivityMetricRepository,
)


def calculate_trend(
    values: list[float],
) -> str:
    """
    Determine whether values are increasing,
    decreasing, or stable.
    """

    if len(values) < 2:
        return "stable"

    if values[-1] > values[0]:
        return "increasing"

    if values[-1] < values[0]:
        return "decreasing"

    return "stable"


def calculate_pace_trend(
    paces: list[float],
) -> str:
    """
    Determine pace improvement.

    Lower pace seconds per km is better.
    """

    if len(paces) < 2:
        return "stable"

    if paces[-1] < paces[0]:
        return "improving"

    if paces[-1] > paces[0]:
        return "declining"

    return "stable"


def generate_performance_trends(
    activities: list[dict],
) -> dict:
    """
    Generate performance trends from activities.
    """

    distances = [
        activity["distance_km"]
        for activity in activities
    ]

    paces = [
        activity["average_pace"]
        for activity in activities
    ]

    loads = [
        activity.get(
            "training_load",
            0,
        )
        for activity in activities
    ]

    return {
        "distance_trend": calculate_trend(
            distances,
        ),
        "pace_trend": calculate_pace_trend(
            paces,
        ),
        "training_load_trend": calculate_trend(
            loads,
        ),
    }


def generate_athlete_performance_trends(
    athlete_id: int,
    repository: ActivityMetricRepository,
) -> dict:
    """
    Generate performance trends from stored athlete metrics.
    """

    metrics = repository.get_by_athlete_id(
        athlete_id,
    )

    activities = [
        {
            "distance_km": metric.distance_km or 0.0,
            "average_pace": metric.average_pace or 0.0,
            "training_load": metric.training_load or 0.0,
        }
        for metric in metrics
    ]

    return generate_performance_trends(
        activities,
    )
