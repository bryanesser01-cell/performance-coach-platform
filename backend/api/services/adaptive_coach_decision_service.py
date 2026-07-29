def generate_coach_decision(
    readiness_score: int,
    training_load_status: str,
    performance_trend: str,
    days_to_race: int | None = None,
) -> dict:
    """
    Generate adaptive coaching decision.
    """

    if (
        days_to_race is not None
        and days_to_race <= 14
        and readiness_score >= 80
    ):
        return {
            "decision": "RACE_TAPER",
            "recommendation": (
                "Reduce training volume and "
                "prioritise freshness."
            ),
            "reason": (
                "Race is approaching with "
                "high readiness."
            ),
        }

    if (
        readiness_score < 60
        or training_load_status == "high_fatigue"
    ):
        return {
            "decision": "REDUCE_TRAINING",
            "recommendation": (
                "Reduce intensity and focus "
                "on recovery."
            ),
            "reason": (
                "Recovery indicators require "
                "attention."
            ),
        }

    if (
        performance_trend == "improving"
        and readiness_score >= 75
    ):
        return {
            "decision": "PROGRESS_TRAINING",
            "recommendation": (
                "Progress training carefully "
                "while maintaining recovery."
            ),
            "reason": (
                "Performance and readiness "
                "are improving."
            ),
        }

    if (
        readiness_score >= 70
        and training_load_status == "stable"
    ):
        return {
            "decision": "MAINTAIN_TRAINING",
            "recommendation": (
                "Continue the current training plan."
            ),
            "reason": (
                "Training load and recovery "
                "are balanced."
            ),
        }

    return {
        "decision": "RECOVERY_SESSION",
        "recommendation": (
            "Complete an easy recovery session."
        ),
        "reason": (
            "Current indicators suggest caution."
        ),
    }
