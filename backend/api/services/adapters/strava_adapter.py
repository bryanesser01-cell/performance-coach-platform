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


def convert_strava_activity(
    strava_data: dict,
) -> dict:
    """
    Convert Strava activity format
    into AI Coach standard format.

    Future compatible with:
    - Strava API
    """

    distance_km = (
        strava_data.get(
            "distance_meters",
            0,
        )
        / 1000
    )

    duration_minutes = (
        strava_data.get(
            "moving_time_seconds",
            0,
        )
        / 60
    )

    return {
        "source": "strava",
        "session_type": "run",
        "activity_id": strava_data.get("activity_id"),
        "date": strava_data.get("date"),
        "distance_km": distance_km,
        "duration_minutes": (duration_minutes),
        "pace": calculate_pace(
            distance_km,
            duration_minutes,
        ),
        "avg_heart_rate": (strava_data.get("average_heartrate")),
        "max_heart_rate": (strava_data.get("max_heartrate")),
        "cadence": (strava_data.get("cadence")),
        "elevation_gain": (strava_data.get("total_elevation_gain")),
    }


def validate_strava_activity(
    activity: dict,
) -> dict:
    """
    Validate Strava conversion.
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


def build_strava_training_record(
    strava_data: dict,
) -> dict:
    """
    Complete Strava import pipeline.

    Strava
      ↓
    Convert
      ↓
    Validate
    """

    activity = convert_strava_activity(
        strava_data,
    )

    validation = validate_strava_activity(
        activity,
    )

    return {
        "training_session": activity,
        "validation": validation,
        "import_complete": (validation["valid"]),
    }
