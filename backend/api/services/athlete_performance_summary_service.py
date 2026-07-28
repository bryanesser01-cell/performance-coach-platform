from database.repositories.activity_metric_repository import (
    ActivityMetricRepository,
)


def calculate_weekly_distance(
    activities: list[dict],
) -> float:
    """
    Calculate total weekly distance.
    """

    return sum(
        activity["distance_km"]
        for activity in activities
    )


def calculate_average_pace(
    activities: list[dict],
) -> float:
    """
    Calculate average pace across activities.
    """

    if not activities:
        return 0.0

    total_distance = sum(
        activity["distance_km"]
        for activity in activities
    )

    total_duration = sum(
        activity["duration_seconds"]
        for activity in activities
    )

    if total_distance == 0:
        return 0.0

    return total_duration / total_distance


def calculate_training_load(
    activities: list[dict],
) -> float:
    """
    Calculate combined training load.
    """

    return sum(
        activity.get(
            "training_load",
            0,
        )
        for activity in activities
    )


def generate_performance_summary(
    activities: list[dict],
) -> dict:
    """
    Generate athlete performance summary.
    """

    return {
        "weekly_distance_km": calculate_weekly_distance(
            activities,
        ),
        "average_pace_seconds_per_km": calculate_average_pace(
            activities,
        ),
        "training_load": calculate_training_load(
            activities,
        ),
    }


def generate_athlete_performance_summary(
    athlete_id: int,
    repository: ActivityMetricRepository,
) -> dict:
    """
    Generate performance summary from stored athlete activity metrics.
    """

    metrics = repository.get_by_athlete_id(
        athlete_id,
    )

    activities = [
        {
            "distance_km": metric.distance_km or 0.0,
            "duration_seconds": metric.duration_seconds or 0.0,
            "training_load": metric.training_load or 0.0,
        }
        for metric in metrics
    ]

    return generate_performance_summary(
        activities,
    )
