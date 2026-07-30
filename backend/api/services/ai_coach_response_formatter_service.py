from api.schemas.ai_coach_response_schema import (
    AICoachResponseSchema,
)


def format_ai_coach_response(
    athlete_id: int,
    question: str,
    coach_response: dict,
) -> dict:
    """
    Convert raw AI Coach output into the
    standard API response contract.
    """

    response = AICoachResponseSchema(
        athlete_id=athlete_id,
        question=question,
        coach_message=coach_response.get(
            "coach_message",
            "",
        ),
        decision=coach_response.get(
            "decision",
        ),
        recommendation=coach_response.get(
            "recommendation",
        ),
        confidence=coach_response.get(
            "confidence",
            0,
        ),
        memory_used=coach_response.get(
            "memory_used",
            False,
        ),
        learning_updated=coach_response.get(
            "learning_updated",
            False,
        ),
        strategy=coach_response.get(
            "strategy",
        ),
        metadata=coach_response.get(
            "metadata",
            {},
        ),
    )

    return response.model_dump()


def build_standard_coach_response(
    athlete_id: int,
    question: str,
    message: str,
    decision: str | None = None,
    recommendation: str | None = None,
    confidence: int = 0,
    memory_used: bool = False,
    learning_updated: bool = False,
    strategy: str | None = None,
) -> dict:
    """
    Build a standard AI Coach response.
    """

    response = AICoachResponseSchema(
        athlete_id=athlete_id,
        question=question,
        coach_message=message,
        decision=decision,
        recommendation=recommendation,
        confidence=confidence,
        memory_used=memory_used,
        learning_updated=learning_updated,
        strategy=strategy,
    )

    return response.model_dump()


def validate_coach_response(
    response: dict,
) -> bool:
    """
    Validate response against the
    AI Coach API contract.
    """

    AICoachResponseSchema(
        **response,
    )

    return True
