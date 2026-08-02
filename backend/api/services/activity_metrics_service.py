def calculate_pace(
    distance_km: float,
    duration_seconds: float,
) -> float:
    """
    Calculate pace in seconds per kilometre.
    """

    if distance_km <= 0:
        raise ValueError("Distance must be greater than zero.")

    return duration_seconds / distance_km


def calculate_speed(
    distance_km: float,
    duration_seconds: float,
) -> float:
    """
    Calculate speed in kilometres per hour.
    """

    if duration_seconds <= 0:
        raise ValueError("Duration must be greater than zero.")

    hours = duration_seconds / 3600

    return distance_km / hours


def calculate_training_load(
    duration_seconds: float,
    average_heart_rate: int | None,
) -> float:
    """
    Calculate simplified training load score.

    Formula:
    duration (minutes) × average HR factor
    """

    if not average_heart_rate:
        return 0.0

    duration_minutes = duration_seconds / 60

    return duration_minutes * (average_heart_rate / 100)


def generate_metric_summary(
    distance_km: float,
    duration_seconds: float,
    average_heart_rate: int | None = None,
) -> dict:
    """
    Generate activity performance summary.
    """

    return {
        "distance_km": distance_km,
        "pace_seconds_per_km": calculate_pace(
            distance_km,
            duration_seconds,
        ),
        "speed_kmh": calculate_speed(
            distance_km,
            duration_seconds,
        ),
        "training_load": calculate_training_load(
            duration_seconds,
            average_heart_rate,
        ),
    }
