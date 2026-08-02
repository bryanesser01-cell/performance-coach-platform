def calculate_pace(
    distance_km: float,
    duration_minutes: float,
) -> str:
    """
    Calculate pace per kilometre.
    """

    if distance_km <= 0:
        return "0:00/km"

    pace = duration_minutes / distance_km

    minutes = int(pace)

    seconds = int(round((pace - minutes) * 60))

    if seconds == 60:
        minutes += 1
        seconds = 0

    return f"{minutes}:{seconds:02d}/km"


def convert_apple_health_workout(
    apple_data: dict,
) -> dict:
    """
    Convert Apple Health workout
    format into AI Coach format.

    Future compatible with:
    - Apple HealthKit
    - Apple Watch workouts
    """

    distance_km = apple_data.get(
        "distance_km",
        0,
    )

    duration_minutes = apple_data.get(
        "duration_minutes",
        0,
    )

    return {
        "source": "apple_health",
        "session_type": "run",
        "workout_id": apple_data.get("workout_id"),
        "date": apple_data.get("date"),
        "distance_km": distance_km,
        "duration_minutes": (duration_minutes),
        "pace": calculate_pace(
            distance_km,
            duration_minutes,
        ),
        "avg_heart_rate": (apple_data.get("heart_rate")),
        "max_heart_rate": (apple_data.get("max_heart_rate")),
        "cadence": (apple_data.get("cadence")),
        "elevation_gain": (apple_data.get("elevation_gain")),
    }


def validate_apple_health_workout(
    workout: dict,
) -> dict:
    """
    Validate Apple Health conversion.
    """

    required_fields = [
        "distance_km",
        "duration_minutes",
        "session_type",
    ]

    missing = []

    for field in required_fields:

        if field not in workout:

            missing.append(field)

    return {
        "valid": len(missing) == 0,
        "missing_fields": missing,
    }


def build_apple_health_record(
    apple_data: dict,
) -> dict:
    """
    Complete Apple Health pipeline.

    Apple Health
          ↓
    Convert
          ↓
    Validate
    """

    workout = convert_apple_health_workout(
        apple_data,
    )

    validation = validate_apple_health_workout(
        workout,
    )

    return {
        "training_session": workout,
        "validation": validation,
        "import_complete": (validation["valid"]),
    }
