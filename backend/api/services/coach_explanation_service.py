def classify_explanation_context(
    age: int,
    event: str,
    training_phase: str,
) -> dict:
    """
    Classify athlete context for explanation.

    Used to explain:
    - why the session exists
    - what adaptation it targets
    """

    if event in [
        "100m",
        "200m",
        "400m",
    ]:

        focus = [
            "speed development",
            "power",
            "running mechanics",
        ]

    elif event in [
        "800m",
        "1500m",
        "mile",
    ]:

        focus = [
            "running economy",
            "speed reserve",
            "race pace ability",
        ]

    elif event in [
        "3000m",
        "5000m",
        "10000m",
        "5K",
        "10K",
    ]:

        focus = [
            "aerobic capacity",
            "threshold",
            "endurance",
        ]

    elif event in [
        "half_marathon",
        "marathon",
    ]:

        focus = [
            "durability",
            "fatigue resistance",
            "fuel efficiency",
        ]

    elif event in [
        "trail",
        "ultra_marathon",
    ]:

        focus = [
            "terrain strength",
            "resilience",
            "long duration endurance",
        ]

    else:

        focus = [
            "general development",
        ]


    if age < 12:

        athlete_message = (
            "Focus on skill development, "
            "coordination and safe progression."
        )

    elif age < 18:

        athlete_message = (
            "Focus on developing athletic "
            "qualities while progressing safely."
        )

    else:

        athlete_message = (
            "Focus on performance optimisation "
            "and managing training load."
        )


    return {
        "event_focus": focus,
        "athlete_message": athlete_message,
        "training_phase": training_phase,
    }



def explain_running_session(
    age: int,
    event: str,
    session: str,
    goal: str,
    training_phase: str = "BUILD",
) -> dict:
    """
    Explain why a running session was prescribed.
    """

    context = classify_explanation_context(
        age=age,
        event=event,
        training_phase=training_phase,
    )


    return {
        "session": session,

        "goal": goal,

        "why_this_session": (
            f"This session supports {event} "
            "performance by developing "
            + ", ".join(
                context["event_focus"]
            )
            + "."
        ),

        "what_to_focus_on": (
            context["event_focus"]
        ),

        "what_you_should_feel": (
            "Controlled effort with good "
            "technique. Finish feeling like "
            "you could complete the session "
            "with quality."
        ),

        "avoid": [
            "Poor technique",
            "Going faster than prescribed",
            "Ignoring fatigue signals",
        ],

        "coach_tip": (
            context["athlete_message"]
        ),
    }



def explain_strength_session(
    age: int,
    event: str,
    exercises: list[str],
) -> dict:
    """
    Explain strength recommendation.
    """

    if age < 14:

        reason = (
            "Strength training develops "
            "movement quality, coordination "
            "and athletic foundations."
        )

    else:

        reason = (
            "Strength training improves "
            "performance qualities such as "
            "power, durability and injury "
            "resilience."
        )


    return {
        "session_type": "strength",

        "exercises": exercises,

        "why_this_session": reason,

        "what_to_focus_on": [
            "Quality movement",
            "Controlled technique",
            "Consistency",
        ],

        "avoid": [
            "Poor technique",
            "Training through pain",
            "Excessive load progression",
        ],

        "coach_tip": (
            "Strength supports running "
            "performance when combined with "
            "appropriate endurance training."
        ),
    }



def build_coach_explanation(
    session_type: str,
    age: int,
    event: str,
    session: str,
    goal: str,
    training_phase: str = "BUILD",
) -> dict:
    """
    Build complete coach explanation.
    """

    if session_type == "strength":

        return explain_strength_session(
            age=age,
            event=event,
            exercises=[
                session,
            ],
        )


    return explain_running_session(
        age=age,
        event=event,
        session=session,
        goal=goal,
        training_phase=training_phase,
    )
