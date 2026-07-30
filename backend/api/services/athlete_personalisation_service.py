def build_athlete_profile(
    athlete_id: int,
    name: str,
    age: int,
    race_distance: str,
    goal: str,
) -> dict:
    """
    Build athlete personalisation profile.

    Stores the key information needed
    for personalised coaching.
    """

    return {
        "athlete_id": athlete_id,
        "name": name,
        "age": age,
        "race_distance": race_distance,
        "goal": goal,
    }


def remember_training_preferences(
    preferred_sessions: list[str],
    disliked_sessions: list[str],
    preferred_training_days: list[str],
) -> dict:
    """
    Store athlete training preferences.
    """

    return {
        "preferred_sessions": preferred_sessions,
        "disliked_sessions": disliked_sessions,
        "preferred_training_days": preferred_training_days,
    }


def apply_athlete_history(
    previous_results: list[dict],
    injury_history: list[str],
    training_response: list[str],
) -> dict:
    """
    Apply previous athlete history.

    Learns what has worked and what
    has caused problems previously.
    """

    return {
        "previous_results": previous_results,
        "injury_history": injury_history,
        "training_response": training_response,
        "history_available": True,
    }


def personalise_daily_recommendation(
    recommendation: dict,
    athlete_profile: dict,
    preferences: dict,
    history: dict,
) -> dict:
    """
    Personalise AI Coach recommendation.

    Adjusts generic recommendations
    based on athlete memory.
    """

    message = recommendation.get(
        "message",
        "",
    )

    if athlete_profile.get(
        "race_distance",
    ) == "1500m":
        message += (
            " Focus on speed, power "
            "and running economy."
        )

    if (
        "injury_history" in history
        and history["injury_history"]
    ):
        message += (
            " Include injury prevention "
            "and mobility work."
        )

    return {
        "athlete_id": athlete_profile[
            "athlete_id"
        ],
        "personalised_message": message,
        "recommendation": recommendation,
        "preferences": preferences,
        "history": history,
    }


def build_personalised_coach_memory(
    athlete_profile: dict,
    preferences: dict,
    history: dict,
) -> dict:
    """
    Combine all athlete memory data
    into a single coaching memory.
    """

    return {
        "athlete_profile": athlete_profile,
        "training_preferences": preferences,
        "athlete_history": history,
        "memory_ready": True,
    }
