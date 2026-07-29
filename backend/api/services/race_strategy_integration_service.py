from api.services.race_strategy_service import (
    generate_race_instruction,
    generate_race_strategy,
)


def build_race_strategy_context(
    athlete_state: dict,
    event: str,
    target_time: str,
) -> dict:
    """
    Build complete race strategy context
    for AI Coach.

    Uses:
    - Athlete state
    - Race goal
    - Target time
    - Event checkpoints
    """

    race_strategy = generate_race_strategy(
        event=event,
        target_time=target_time,
    )

    instructions = generate_race_instruction(
        event,
    )

    athlete = athlete_state.get(
        "athlete",
        {},
    )

    readiness = athlete_state.get(
        "readiness",
        {},
    )

    performance = athlete_state.get(
        "performance",
        {},
    )

    return {
        "athlete": {
            "name": athlete.get(
                "name",
                "Athlete",
            ),
            "event": event,
        },
        "race_goal": {
            "target_time": target_time,
        },
        "race_strategy": race_strategy,
        "instructions": instructions,
        "readiness": readiness,
        "performance": performance,
    }


def generate_race_coach_message(
    race_context: dict,
) -> str:
    """
    Convert race strategy into
    AI Coach message.
    """

    event = race_context[
        "race_strategy"
    ].get(
        "event",
        "race",
    )

    target = race_context[
        "race_goal"
    ].get(
        "target_time",
        "",
    )

    checkpoints = race_context[
        "race_strategy"
    ].get(
        "checkpoints",
        [],
    )

    if not checkpoints:
        return (
            f"Your {event} race plan "
            f"is targeting {target}."
        )

    first_checkpoint = checkpoints[0]

    return (
        f"Your {event} race target is "
        f"{target}. "
        f"Your opening checkpoint is "
        f"{first_checkpoint['distance']}m "
        f"in {first_checkpoint['cumulative_time']}."
    )


def should_adjust_race_strategy(
    athlete_state: dict,
) -> bool:
    """
    Determine if race strategy
    should be adjusted.

    Uses readiness.
    """

    readiness = athlete_state.get(
        "readiness",
        {},
    )

    score = readiness.get(
        "score",
        0,
    )

    return score < 60
