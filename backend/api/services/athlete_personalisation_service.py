def classify_athlete_development_stage(
    age: int,
    training_age_years: float,
    experience_level: str,
) -> dict:
    """
    Classify athlete development stage.

    Uses:
    - chronological age
    - training age
    - experience
    """

    if age < 12:

        stage = "YOUTH_DEVELOPMENT"

    elif age < 18:

        stage = "JUNIOR_PERFORMANCE"

    elif age < 35:

        stage = "ADULT_PERFORMANCE"

    else:

        stage = "MASTERS_PERFORMANCE"

    return {
        "age": age,
        "training_age_years": training_age_years,
        "experience_level": experience_level,
        "development_stage": stage,
    }


def build_athlete_profile(
    athlete_id: int,
    name: str,
    age: int,
    race_distance: str,
    goal: str,
    training_age_years: float = 0,
    experience_level: str = "developing",
    weekly_training_volume_km: float = 0,
    personal_bests: dict | None = None,
) -> dict:
    """
    Build athlete personalisation profile.

    Stores the key information needed
    for personalised coaching.
    """

    development = classify_athlete_development_stage(
        age=age,
        training_age_years=training_age_years,
        experience_level=experience_level,
    )

    return {
        "athlete_id": athlete_id,
        "name": name,
        "age": age,
        "race_distance": race_distance,
        "goal": goal,
        "training_age_years": (training_age_years),
        "experience_level": (experience_level),
        "weekly_training_volume_km": (weekly_training_volume_km),
        "personal_bests": (personal_bests or {}),
        "development_stage": development["development_stage"],
    }


def remember_training_preferences(
    preferred_sessions: list[str],
    disliked_sessions: list[str],
    preferred_training_days: list[str],
    available_training_days: list[str] | None = None,
) -> dict:
    """
    Store athlete training preferences.
    """

    return {
        "preferred_sessions": preferred_sessions,
        "disliked_sessions": disliked_sessions,
        "preferred_training_days": (preferred_training_days),
        "available_training_days": (available_training_days or []),
    }


def apply_athlete_history(
    previous_results: list[dict],
    injury_history: list[str],
    training_response: list[str],
    fatigue_patterns: list[str] | None = None,
) -> dict:
    """
    Apply previous athlete history.

    Learns:
    - what works
    - injury risks
    - fatigue patterns
    """

    return {
        "previous_results": previous_results,
        "injury_history": injury_history,
        "training_response": training_response,
        "fatigue_patterns": (fatigue_patterns or []),
        "history_available": True,
    }


def analyse_athlete_constraints(
    athlete_profile: dict,
    history: dict,
) -> dict:
    """
    Identify coaching constraints.
    """

    constraints = []

    if history.get(
        "injury_history",
    ):

        constraints.append("injury_management")

    if (
        athlete_profile.get(
            "weekly_training_volume_km",
            0,
        )
        < 10
    ):

        constraints.append("build_training_capacity")

    if (
        athlete_profile.get(
            "development_stage",
        )
        == "YOUTH_DEVELOPMENT"
    ):

        constraints.append("age_appropriate_progression")

    return {
        "constraints": constraints,
    }


def personalise_daily_recommendation(
    recommendation: dict,
    athlete_profile: dict,
    preferences: dict,
    history: dict,
) -> dict:
    """
    Personalise AI Coach recommendation.

    Adjusts recommendations based on:
    - event
    - age
    - experience
    - history
    - preferences
    """

    message = recommendation.get(
        "message",
        "",
    )

    event = athlete_profile.get(
        "race_distance",
        "",
    )

    age = athlete_profile.get(
        "age",
    )

    if event == "1500m":

        message += " Focus on running economy, " "speed development and power."

    if event in [
        "marathon",
        "half_marathon",
    ]:

        message += " Prioritise endurance, " "durability and recovery."

    if event in [
        "trail",
        "ultra_marathon",
    ]:

        message += " Include terrain adaptation, " "strength endurance and resilience."

    if age and age < 12:

        message += (
            " Training should prioritise " "skill development and safe progression."
        )

    if history.get(
        "injury_history",
    ):

        message += " Include injury prevention " "and mobility work."

    constraints = analyse_athlete_constraints(
        athlete_profile,
        history,
    )

    return {
        "athlete_id": athlete_profile["athlete_id"],
        "personalised_message": message,
        "recommendation": recommendation,
        "preferences": preferences,
        "history": history,
        "constraints": constraints,
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
