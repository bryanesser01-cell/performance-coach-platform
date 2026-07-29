from api.services.adaptive_coach_decision_service import (
    generate_coach_decision,
)


def generate_ai_coach_decision_response(
    athlete_id: int,
    question: str,
    readiness_score: int,
    training_load_status: str,
    performance_trend: str,
    days_to_race: int | None = None,
) -> dict:
    """
    Generate an AI coach decision response.

    Connects athlete question with the
    adaptive coaching decision engine.
    """

    decision = generate_coach_decision(
        readiness_score=readiness_score,
        training_load_status=training_load_status,
        performance_trend=performance_trend,
        days_to_race=days_to_race,
    )

    coach_message = build_coach_message(
        question=question,
        decision=decision,
    )

    return {
        "athlete_id": athlete_id,
        "question": question,
        "decision": decision["decision"],
        "recommendation": decision["recommendation"],
        "reason": decision["reason"],
        "coach_message": coach_message,
    }


def build_coach_message(
    question: str,
    decision: dict,
) -> str:
    """
    Convert decision engine output into
    athlete-friendly coaching language.
    """

    return (
        f"Regarding '{question}', "
        f"{decision['recommendation']} "
        f"Reason: {decision['reason']}"
    )
