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


def convert_coros_activity(
    coros_data: dict,
) -> dict:
    """
    Convert COROS activity format
    into AI Coach standard format.

    Future compatible with:
    - COROS API
    - COROS Training Hub
    """

    distance_km = coros_data.get(
        "distance_km",
        0,
    )

    duration_minutes = coros_data.get(
        "duration_minutes",
        0,
    )

    return {
        "source": "coros",
        "session_type": "run",
        "activity_id": coros_data.get("activity_id"),
        "date": coros_data.get("date"),
        "distance_km": distance_km,
        "duration_minutes": (duration_minutes),
        "pace": calculate_pace(
            distance_km,
            duration_minutes,
        ),
        "avg_heart_rate": (coros_data.get("average_hr")),
        "max_heart_rate": (coros_data.get("max_hr")),
        "cadence": (coros_data.get("cadence")),
        "elevation_gain": (coros_data.get("elevation_gain")),
    }


def validate_coros_activity(
    activity: dict,
) -> dict:
    """
    Validate COROS conversion.
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


def build_coros_training_record(
    coros_data: dict,
) -> dict:
    """
    Complete COROS import pipeline.

    COROS
      ↓
    Convert
      ↓
    Validate
    """

    activity = convert_coros_activity(
        coros_data,
    )

    validation = validate_coros_activity(
        activity,
    )

    return {
        "training_session": activity,
        "validation": validation,
        "import_complete": (validation["valid"]),
    }
