def build_coach_prompt(
    question: str,
    athlete_state: dict,
    memory_context: dict | None = None,
    voice_memory_context: dict | None = None,
    training_memory: dict | None = None,
    coach_decision: dict | None = None,
    race_strategy_context: dict | None = None,
) -> dict:
    """
    Build complete AI coach prompt context.

    Includes:
    - Athlete state
    - Long term memory
    - Voice history
    - Training history
    - Coaching decision
    """

    return {
        "question": question,
        "athlete_state": athlete_state,
        "memory_context": (memory_context if memory_context else {}),
        "voice_memory": (voice_memory_context if voice_memory_context else {}),
        "training_memory": (training_memory if training_memory else {}),
        "coach_decision": (coach_decision if coach_decision else {}),
        "race_strategy": (race_strategy_context if race_strategy_context else {}),
    }


def generate_prompt_summary(
    prompt_context: dict,
) -> str:
    """
    Generate human readable prompt summary.
    """

    athlete_state = prompt_context.get(
        "athlete_state",
        {},
    )

    athlete = athlete_state.get(
        "athlete",
        {},
    )

    readiness = athlete_state.get(
        "readiness",
        {},
    )

    return (
        f"{athlete.get('name', 'Athlete')} "
        f"is training for "
        f"{athlete.get('primary_event', 'event')}. "
        f"Current readiness is "
        f"{readiness.get('score', 0)}."
    )


def has_voice_memory(
    prompt_context: dict,
) -> bool:
    """
    Check voice history exists.
    """

    return prompt_context.get(
        "voice_memory",
        {},
    ).get(
        "has_history",
        False,
    )


def has_training_memory(
    prompt_context: dict,
) -> bool:
    """
    Check training history exists.
    """

    return prompt_context.get(
        "training_memory",
        {},
    ).get(
        "has_training_history",
        False,
    )


def has_race_strategy(
    prompt_context: dict,
) -> bool:
    """
    Check if race strategy
    context exists.
    """

    return bool(
        prompt_context.get(
            "race_strategy",
            {},
        )
    )
