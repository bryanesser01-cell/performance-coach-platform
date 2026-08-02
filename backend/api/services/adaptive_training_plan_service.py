def adapt_training_plan(
    current_plan: dict,
    completed_sessions: int,
    missed_sessions: int,
    fatigue_level: str,
) -> dict:
    """
    Adapt training plan based on athlete response.

    Rules:
    - High fatigue reduces load
    - Missed sessions reduce progression
    - Completed sessions maintain progression
    """

    adjusted_plan = current_plan.copy()

    if fatigue_level == "high":
        return {
            **adjusted_plan,
            "adjustment": "reduce_load",
            "message": (
                "Fatigue detected. Reduce training intensity "
                "and prioritise recovery."
            ),
        }

    if missed_sessions > 1:
        return {
            **adjusted_plan,
            "adjustment": "maintain",
            "message": (
                "Missed sessions detected. Maintain current "
                "training load before progressing."
            ),
        }

    if completed_sessions >= 3:
        return {
            **adjusted_plan,
            "adjustment": "progress",
            "message": (
                "Training consistency is good. " "Progress training gradually."
            ),
        }

    return {
        **adjusted_plan,
        "adjustment": "maintain",
        "message": ("Continue current training plan."),
    }
