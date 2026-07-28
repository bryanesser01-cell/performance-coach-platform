def calculate_race_readiness_score(
    training_load: float,
    performance_score: float,
    fatigue_score: float,
    consistency_score: float,
) -> int:
    """
    Calculate race readiness score.

    Higher scores indicate better race preparedness.
    """

    score = (
        (training_load * 0.25)
        + (performance_score * 0.35)
        + (fatigue_score * 0.20)
        + (consistency_score * 0.20)
    )

    return round(
        min(
            max(score, 0),
            100,
        )
    )


def get_readiness_status(
    score: int,
) -> str:
    """
    Convert readiness score into status.
    """

    if score >= 90:
        return "excellent"

    if score >= 75:
        return "ready"

    if score >= 50:
        return "developing"

    return "needs_recovery"


def generate_race_readiness_report(
    training_load: float,
    performance_score: float,
    fatigue_score: float,
    consistency_score: float,
) -> dict:
    """
    Generate race readiness report.
    """

    score = calculate_race_readiness_score(
        training_load,
        performance_score,
        fatigue_score,
        consistency_score,
    )

    status = get_readiness_status(
        score,
    )

    return {
        "race_readiness_score": score,
        "status": status,
        "recommendation": (
            "Maintain intensity and reduce volume."
            if status in ["excellent", "ready"]
            else "Continue building fitness and recovery."
        ),
    }
