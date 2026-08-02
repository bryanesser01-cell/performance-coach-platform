def generate_recommendation(
    status: str,
    pace_trend: str,
    training_load_trend: str,
) -> dict:
    """
    Generate training recommendation from athlete trends.
    """

    if training_load_trend == "increasing":
        return {
            "recommendation": "monitor_recovery",
            "message": (
                "Training load is increasing. " "Monitor fatigue and recovery."
            ),
        }

    if status == "progressing" and pace_trend == "improving":
        return {
            "recommendation": "continue_progression",
            "message": (
                "Fitness is improving. " "Continue current training progression."
            ),
        }

    if pace_trend == "declining":
        return {
            "recommendation": "reduce_load",
            "message": (
                "Performance is declining. " "Consider reducing training load."
            ),
        }

    return {
        "recommendation": "maintain",
        "message": (
            "Maintain current training approach " "and continue monitoring progress."
        ),
    }
