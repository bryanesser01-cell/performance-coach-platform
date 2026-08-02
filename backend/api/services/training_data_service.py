from datetime import date


def calculate_running_pace(
    distance_km: float,
    duration_minutes: float,
) -> str:
    """
    Calculate running pace per kilometre.
    """

    if distance_km <= 0:
        return "0:00/km"

    pace_minutes = duration_minutes / distance_km

    minutes = int(pace_minutes)

    seconds = int(round((pace_minutes - minutes) * 60))

    if seconds == 60:
        minutes += 1
        seconds = 0

    return f"{minutes}:{seconds:02d}/km"


def calculate_session_load(
    duration_minutes: float,
    intensity: int,
) -> int:
    """
    Calculate simple training load.

    Load =
    duration x intensity
    """

    return int(duration_minutes * intensity)


def create_training_session(
    session_date: str,
    distance_km: float,
    duration_minutes: float,
    avg_heart_rate: int | None = None,
    max_heart_rate: int | None = None,
    cadence: int | None = None,
    elevation_gain: int | None = None,
    intensity: int = 1,
    athlete_feedback: str = "",
) -> dict:
    """
    Create standard training data format.

    Works with:
    - Garmin
    - Apple Watch
    - Coros
    - Manual entry
    """

    return {
        "date": session_date,
        "session_type": "run",
        "distance_km": distance_km,
        "duration_minutes": duration_minutes,
        "pace": calculate_running_pace(
            distance_km,
            duration_minutes,
        ),
        "avg_heart_rate": avg_heart_rate,
        "max_heart_rate": max_heart_rate,
        "cadence": cadence,
        "elevation_gain": elevation_gain,
        "training_load": calculate_session_load(
            duration_minutes,
            intensity,
        ),
        "athlete_feedback": athlete_feedback,
    }


def summarise_training_week(
    sessions: list[dict],
) -> dict:
    """
    Summarise recent training.
    """

    total_distance = 0
    total_duration = 0
    total_load = 0

    for session in sessions:

        total_distance += session.get(
            "distance_km",
            0,
        )

        total_duration += session.get(
            "duration_minutes",
            0,
        )

        total_load += session.get(
            "training_load",
            0,
        )

    return {
        "sessions_completed": len(sessions),
        "total_distance_km": (total_distance),
        "total_duration_minutes": (total_duration),
        "total_training_load": (total_load),
    }


def analyse_training_response(
    sessions: list[dict],
) -> dict:
    """
    Analyse athlete feedback.
    """

    positive = []
    negative = []

    for session in sessions:

        feedback = session.get(
            "athlete_feedback",
            "",
        ).lower()

        if feedback in [
            "good",
            "strong",
            "easy",
        ]:

            positive.append(session["date"])

        elif feedback in [
            "tired",
            "fatigued",
            "hard",
        ]:

            negative.append(session["date"])

    return {
        "positive_sessions": positive,
        "challenging_sessions": negative,
        "patterns_available": True,
    }


def build_training_data_record(
    athlete_id: int,
    sessions: list[dict],
) -> dict:
    """
    Build athlete training record.
    """

    return {
        "athlete_id": athlete_id,
        "sessions": sessions,
        "summary": summarise_training_week(sessions),
        "response_analysis": (analyse_training_response(sessions)),
        "created_date": str(date.today()),
    }
