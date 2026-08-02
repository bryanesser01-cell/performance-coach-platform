"""
Coach Learning Service

Responsible for:
- analysing athlete training responses
- identifying training patterns
- updating athlete learning profiles
- analysing coaching decision outcomes
"""


def analyse_training_session_response(
    session: dict,
) -> dict:
    """
    Analyse athlete response after training.
    """

    feedback = session.get(
        "athlete_feedback",
        "",
    ).lower()

    if feedback in [
        "good",
        "strong",
        "easy",
        "comfortable",
    ]:

        response = "POSITIVE"

    elif feedback in [
        "tired",
        "fatigued",
        "hard",
        "struggled",
    ]:

        response = "NEGATIVE"

    else:

        response = "UNKNOWN"

    return {
        "session_type": session.get(
            "session_type",
        ),
        "response": response,
        "date": session.get(
            "date",
        ),
    }


def identify_training_patterns(
    sessions: list[dict],
) -> dict:
    """
    Identify athlete response patterns.
    """

    responds_well_to = []

    struggles_with = []

    for session in sessions:

        analysis = analyse_training_session_response(
            session,
        )

        if analysis["response"] == "POSITIVE":

            responds_well_to.append(
                analysis["session_type"],
            )

        elif analysis["response"] == "NEGATIVE":

            struggles_with.append(
                analysis["session_type"],
            )

    return {
        "responds_well_to": responds_well_to,
        "struggles_with": struggles_with,
        "patterns_identified": True,
    }


def update_athlete_learning_profile(
    athlete_profile: dict,
    sessions: list[dict],
) -> dict:
    """
    Update athlete learning profile.
    """

    patterns = identify_training_patterns(
        sessions,
    )

    return {
        "athlete_profile": athlete_profile,
        "training_patterns": patterns,
        "learning_updated": True,
    }


def generate_coach_learning_insight(
    learning_profile: dict,
) -> dict:
    """
    Generate coach learning insight.
    """

    patterns = learning_profile.get(
        "training_patterns",
        {},
    )

    return {
        "insight": {
            "strengths": patterns.get(
                "responds_well_to",
                [],
            ),
            "challenges": patterns.get(
                "struggles_with",
                [],
            ),
        },
        "coach_message": (
            "Future training will be " "adapted using athlete response " "history."
        ),
    }


def build_learning_loop_result(
    athlete_profile: dict,
    sessions: list[dict],
) -> dict:
    """
    Complete AI learning loop.
    """

    profile = update_athlete_learning_profile(
        athlete_profile,
        sessions,
    )

    insight = generate_coach_learning_insight(
        profile,
    )

    return {
        "learning_profile": profile,
        "coach_insight": insight,
        "ready_for_future_training": True,
    }


def analyse_coach_decision_outcome(
    decision: str,
    completed: bool,
    athlete_rpe: int | None = None,
    fatigue_after: str | None = None,
) -> dict:
    """
    Analyse whether a coaching decision
    produced a positive or negative result.

    Positive:
    - completed session
    - low RPE
    - low fatigue

    Negative:
    - incomplete session
    - high RPE
    - high fatigue
    """

    if not completed:

        signal = "negative"

    elif athlete_rpe is not None and athlete_rpe <= 5 and fatigue_after == "low":

        signal = "positive"

    elif athlete_rpe is not None and athlete_rpe >= 8 and fatigue_after == "high":

        signal = "negative"

    else:

        signal = "neutral"

    if signal == "positive":

        confidence_update = 1

    elif signal == "negative":

        confidence_update = -1

    else:

        confidence_update = 0

    return {
        "decision": decision,
        "completed": completed,
        "athlete_rpe": athlete_rpe,
        "fatigue_after": fatigue_after,
        "signal": signal,
        "confidence_update": confidence_update,
    }
