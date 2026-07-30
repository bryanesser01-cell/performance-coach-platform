def calculate_readiness_score(
    sleep_score: int,
    soreness_score: int,
    energy_score: int,
    motivation_score: int,
    training_load: int = 0,
) -> int:
    """
    Calculate athlete readiness score.

    Inputs:
    - Sleep score (0-100)
    - Soreness score (0-100)
    - Energy score (0-100)
    - Motivation score (0-100)
    - Training load

    Returns:
    - Readiness score 0-100
    """

    recovery_score = (
        sleep_score
        + (100 - soreness_score)
        + energy_score
        + motivation_score
    ) / 4

    load_penalty = 0

    if training_load >= 500:
        load_penalty = 20

    elif training_load >= 300:
        load_penalty = 10

    readiness = int(
        recovery_score - load_penalty
    )

    return max(
        0,
        min(
            readiness,
            100,
        ),
    )


def analyse_recovery_status(
    readiness_score: int,
) -> dict:
    """
    Categorise recovery state.
    """

    if readiness_score >= 80:
        status = "excellent"

        message = (
            "Athlete is ready for quality training."
        )

    elif readiness_score >= 60:
        status = "good"

        message = (
            "Normal training can continue."
        )

    elif readiness_score >= 40:
        status = "moderate"

        message = (
            "Monitor fatigue and avoid excessive intensity."
        )

    else:
        status = "poor"

        message = (
            "Recovery required before hard training."
        )

    return {
        "status": status,
        "message": message,
    }


def generate_recovery_recommendation(
    readiness_score: int,
) -> dict:
    """
    Generate AI Coach recovery recommendation.
    """

    recovery = analyse_recovery_status(
        readiness_score,
    )

    if recovery["status"] == "excellent":

        recommendation = (
            "Proceed with planned quality session."
        )

    elif recovery["status"] == "good":

        recommendation = (
            "Complete planned training but monitor effort."
        )

    elif recovery["status"] == "moderate":

        recommendation = (
            "Reduce intensity and focus on aerobic work."
        )

    else:

        recommendation = (
            "Take a recovery day or complete easy movement."
        )

    return {
        "readiness_score": readiness_score,
        "status": recovery["status"],
        "recommendation": recommendation,
    }
