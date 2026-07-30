def _convert_time_to_seconds(
    time_value: str,
) -> int:
    """
    Convert race time into seconds.

    Supports:
    MM:SS
    HH:MM:SS
    """

    parts = time_value.split(":")

    if len(parts) == 2:
        minutes, seconds = parts

        return (
            int(minutes) * 60
            + int(seconds)
        )

    if len(parts) == 3:
        hours, minutes, seconds = parts

        return (
            int(hours) * 3600
            + int(minutes) * 60
            + int(seconds)
        )

    raise ValueError(
        "Invalid time format. Use MM:SS or HH:MM:SS"
    )


def create_training_plan(
    goal: str,
    event: str,
    weeks: int,
    current_time: str,
    target_time: str,
) -> dict:
    """
    Create adaptive training plan.

    Builds phases based on:
    - goal
    - event
    - timeline
    """

    if weeks >= 12:

        phases = [
            {
                "phase": "BASE",
                "weeks": "1-4",
                "focus": [
                    "aerobic development",
                    "strength foundation",
                    "running economy",
                ],
            },
            {
                "phase": "BUILD",
                "weeks": "5-8",
                "focus": [
                    "race specific sessions",
                    "threshold work",
                    "speed development",
                ],
            },
            {
                "phase": "PEAK",
                "weeks": "9-11",
                "focus": [
                    "race intensity",
                    "performance sharpening",
                ],
            },
            {
                "phase": "TAPER",
                "weeks": "12",
                "focus": [
                    "recovery",
                    "maintain speed",
                ],
            },
        ]

    else:

        phases = [
            {
                "phase": "SHORT_BUILD",
                "focus": [
                    "fitness improvement",
                    "consistent training",
                ],
            }
        ]

    return {
        "goal": goal,
        "event": event,
        "timeline_weeks": weeks,
        "current_time": current_time,
        "target_time": target_time,
        "phases": phases,
    }


def adjust_weekly_load(
    previous_load: int,
    performance_response: str,
) -> dict:
    """
    Adjust weekly training load.

    Improves:
        +10%

    Fatigue:
        -20%

    Stable:
        unchanged
    """

    if performance_response == "improving":
        change = 10

    elif performance_response == "fatigued":
        change = -20

    else:
        change = 0

    new_load = int(
        previous_load
        * (1 + change / 100)
    )

    return {
        "previous_load": previous_load,
        "change_percent": change,
        "new_load": new_load,
    }


def adapt_plan_from_results(
    race_result: str,
    target_result: str,
    fatigue_score: int,
) -> dict:
    """
    Adapt training plan from race result.

    Faster race times are lower values.

    Example:

    Result:
    4:55

    Target:
    5:00

    Athlete exceeded goal.
    """

    race_seconds = _convert_time_to_seconds(
        race_result,
    )

    target_seconds = _convert_time_to_seconds(
        target_result,
    )

    if fatigue_score > 70:

        action = "REDUCE_LOAD"

    elif race_seconds <= target_seconds:

        action = "CONTINUE_PROGRESS"

    else:

        action = "MODIFY_PLAN"

    return {
        "race_result": race_result,
        "target_result": target_result,
        "race_seconds": race_seconds,
        "target_seconds": target_seconds,
        "fatigue_score": fatigue_score,
        "action": action,
    }


def generate_race_preparation_plan(
    event: str,
    race_date: str,
    goal: str,
) -> dict:
    """
    Generate race preparation strategy.
    """

    return {
        "event": event,
        "race_date": race_date,
        "goal": goal,
        "strategy": [
            "build fitness",
            "race specific preparation",
            "taper before race",
        ],
    }
