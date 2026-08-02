def calculate_pace(
    distance_km: float,
    duration_minutes: float,
) -> str:
    """
    Calculate pace per km.
    """

    if distance_km <= 0:
        return "0:00/km"

    pace = duration_minutes / distance_km

    minutes = int(pace)

    seconds = int(round((pace - minutes) * 60))

    return f"{minutes}:{seconds:02d}/km"


def create_manual_training_entry(
    date: str,
    distance_km: float,
    duration_minutes: float,
    session_type: str = "run",
    event: str | None = None,
    athlete_feedback: str = "",
    notes: str = "",
) -> dict:
    """
    Convert manual athlete entry
    into standard training format.
    """

    return {
        "source": "manual",
        "date": date,
        "session_type": session_type,
        "event": event,
        "distance_km": distance_km,
        "duration_minutes": duration_minutes,
        "pace": calculate_pace(
            distance_km,
            duration_minutes,
        ),
        "athlete_feedback": athlete_feedback,
        "notes": notes,
    }


def create_manual_race_result(
    date: str,
    event: str,
    result_time: str,
    distance_km: float,
    notes: str = "",
) -> dict:
    """
    Store manual race results.

    Used for:
    - track
    - cross country
    - school races
    """

    return {
        "source": "manual",
        "date": date,
        "session_type": "race",
        "event": event,
        "result_time": result_time,
        "distance_km": distance_km,
        "notes": notes,
    }
