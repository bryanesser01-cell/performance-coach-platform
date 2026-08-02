def store_race_result(
    event: str,
    result_time: str,
    race_date: str,
    conditions: str = "",
) -> dict:
    """
    Store athlete race performance.
    """

    return {
        "event": event,
        "result_time": result_time,
        "race_date": race_date,
        "conditions": conditions,
    }


def calculate_personal_best_status(
    current_result: str,
    previous_best: str,
) -> dict:
    """
    Compare current performance against PB.
    """

    def convert_time(
        value: str,
    ) -> int:

        minutes, seconds = value.split(":")

        return int(minutes) * 60 + int(seconds)

    current_seconds = convert_time(
        current_result,
    )

    previous_seconds = convert_time(
        previous_best,
    )

    improved = current_seconds < previous_seconds

    return {
        "current_result": current_result,
        "previous_best": previous_best,
        "personal_best_improved": improved,
        "difference_seconds": (previous_seconds - current_seconds),
    }


def store_training_response(
    session_type: str,
    response: str,
    notes: str = "",
) -> dict:
    """
    Store how athlete responded
    to training.
    """

    return {
        "session_type": session_type,
        "response": response,
        "notes": notes,
    }


def analyse_training_patterns(
    training_history: list[dict],
) -> dict:
    """
    Identify athlete patterns.
    """

    successful_sessions = []

    difficult_sessions = []

    for session in training_history:

        if session.get("response") == "positive":

            successful_sessions.append(session["session_type"])

        elif session.get("response") == "negative":

            difficult_sessions.append(session["session_type"])

    return {
        "successful_sessions": successful_sessions,
        "difficult_sessions": difficult_sessions,
        "patterns_found": True,
    }


def build_performance_memory(
    athlete_profile: dict,
    race_results: list[dict],
    training_history: list[dict],
) -> dict:
    """
    Build complete athlete memory.
    """

    patterns = analyse_training_patterns(
        training_history,
    )

    return {
        "athlete_profile": athlete_profile,
        "race_history": race_results,
        "training_history": training_history,
        "performance_patterns": patterns,
        "memory_ready": True,
    }


def generate_memory_coach_insight(
    performance_memory: dict,
) -> dict:
    """
    Generate coaching insight
    from athlete history.
    """

    patterns = performance_memory.get(
        "performance_patterns",
        {},
    )

    successful = patterns.get(
        "successful_sessions",
        [],
    )

    difficult = patterns.get(
        "difficult_sessions",
        [],
    )

    return {
        "athlete_learning": {
            "responds_well_to": successful,
            "struggles_with": difficult,
        },
        "coach_message": (
            "Future training recommendations "
            "will consider previous athlete "
            "responses and performance history."
        ),
    }
