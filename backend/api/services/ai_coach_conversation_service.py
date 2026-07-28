from sqlalchemy.orm import Session

from api.services.ai_coach_engine_service import (
    generate_ai_coach_response,
)


def generate_coach_conversation_response(
    db: Session,
    athlete_id: int,
    question: str,
) -> dict:
    """
    Generate conversational AI coach response.
    """

    coach_response = generate_ai_coach_response(
        db,
        athlete_id,
    )

    question_lower = question.lower()

    if "train" in question_lower:
        advice = (
            "Your training should follow your current "
            "fitness trend and recovery status."
        )

    elif "race" in question_lower:
        advice = (
            "Your race preparation should focus on "
            "maintaining fitness and arriving fresh."
        )

    elif "recover" in question_lower:
        advice = (
            "Recovery is important to absorb your "
            "recent training improvements."
        )

    else:
        advice = coach_response.get(
            "coach_message",
            "Continue following your training plan.",
        )

    return {
        "athlete_id": athlete_id,
        "question": question,
        "answer": advice,
        "recommendation": coach_response.get(
            "recommendation",
        ),
    }
