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


def convert_garmin_activity(
    garmin_data: dict,
) -> dict:
    """
    Convert Garmin activity format
    into AI Coach standard format.

    Future compatible with:
    - Garmin Connect API
    - Garmin Health API
    """

    distance_km = (
        garmin_data.get(
            "distance_meters",
            0,
        )
        / 1000
    )

    duration_minutes = (
        garmin_data.get(
            "duration_seconds",
            0,
        )
        / 60
    )

    return {
        "source": "garmin",
        "session_type": "run",
        "activity_id": garmin_data.get("activity_id"),
        "date": garmin_data.get("date"),
        "distance_km": distance_km,
        "duration_minutes": (duration_minutes),
        "pace": calculate_pace(
            distance_km,
            duration_minutes,
        ),
        "avg_heart_rate": (garmin_data.get("average_hr")),
        "max_heart_rate": (garmin_data.get("max_hr")),
        "cadence": (garmin_data.get("cadence")),
        "elevation_gain": (garmin_data.get("elevation_gain")),
    }


def validate_garmin_activity(
    activity: dict,
) -> dict:
    """
    Validate Garmin conversion.
    """

    required_fields = [
        "distance_km",
        "duration_minutes",
        "session_type",
    ]

    missing = []

    for field in required_fields:

        if field not in activity:

            missing.append(field)

    return {
        "valid": len(missing) == 0,
        "missing_fields": missing,
    }


def build_garmin_training_record(
    garmin_data: dict,
) -> dict:
    """
    Complete Garmin import pipeline.

    Garmin
      ↓
    Convert
      ↓
    Validate
    """

    activity = convert_garmin_activity(
        garmin_data,
    )

    validation = validate_garmin_activity(
        activity,
    )

    return {
        "training_session": activity,
        "validation": validation,
        "import_complete": (validation["valid"]),
    }
