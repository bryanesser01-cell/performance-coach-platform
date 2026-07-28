from datetime import date


def calculate_training_phase(
    race_date: date,
    current_date: date,
) -> str:
    """
    Determine race preparation phase based on weeks remaining.
    """

    days_until_race = (
        race_date - current_date
    ).days

    weeks_until_race = days_until_race / 7

    if weeks_until_race > 8:
        return "base"

    if weeks_until_race > 6:
        return "build"

    if weeks_until_race > 2:
        return "peak"

    return "taper"


def generate_race_preparation_plan(
    race_date: date,
    current_date: date,
    target_time_seconds: int,
) -> dict:
    """
    Generate race preparation strategy.
    """

    phase = calculate_training_phase(
        race_date,
        current_date,
    )

    return {
        "race_date": race_date.isoformat(),
        "target_time_seconds": target_time_seconds,
        "training_phase": phase,
        "recommendation": get_phase_recommendation(
            phase,
        ),
    }


def get_phase_recommendation(
    phase: str,
) -> str:
    """
    Return training focus for race phase.
    """

    recommendations = {
        "base": (
            "Build aerobic fitness and "
            "increase training consistency."
        ),
        "build": (
            "Increase race-specific workouts "
            "and improve threshold fitness."
        ),
        "peak": (
            "Focus on race intensity and "
            "maintain fitness."
        ),
        "taper": (
            "Reduce training volume and "
            "arrive fresh for race day."
        ),
    }

    return recommendations.get(
        phase,
        "Maintain current training approach.",
    )
