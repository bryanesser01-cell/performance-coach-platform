from database.models import Goal


def analyse_goal_progress(
    goal: Goal,
):
    """
    Analyse athlete goal progress.
    """

    if goal.target_value == 0:
        return {
            "goal_id": goal.id,
            "status": "invalid",
            "message": "Target value cannot be zero.",
        }

    if goal.goal_type.lower() in [
        "5k",
        "10k",
        "half_marathon",
        "marathon",
    ]:
        progress = (
            goal.target_value / goal.current_value
        ) * 100
    else:
        progress = (
            goal.current_value / goal.target_value
        ) * 100

    progress = min(
        round(progress, 2),
        100,
    )

    if progress >= 90:
        status = "almost_complete"
    elif progress >= 70:
        status = "progressing"
    elif progress >= 40:
        status = "building"
    else:
        status = "early_stage"

    return {
        "goal_id": goal.id,
        "goal_type": goal.goal_type,
        "target_value": goal.target_value,
        "current_value": goal.current_value,
        "progress_percentage": progress,
        "status": status,
    }
