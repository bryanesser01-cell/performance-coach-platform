from sqlalchemy.orm import Session

from api.services.athlete_memory_service import (
    build_memory_context,
    recall,
)


def get_ai_coach_memory_context(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Build athlete context for AI Coach.

    Retrieves stored athlete memories and
    converts them into AI-ready context.
    """

    memories = recall(
        db=db,
        athlete_id=athlete_id,
    )

    return build_memory_context(
        memories,
    )


def enrich_coach_prompt(
    db: Session,
    athlete_id: int,
    question: str,
) -> dict:
    """
    Combine athlete memory context with
    athlete question for AI coaching.
    """

    memory_context = get_ai_coach_memory_context(
        db=db,
        athlete_id=athlete_id,
    )

    return {
        "athlete_id": athlete_id,
        "question": question,
        "memory_context": memory_context,
    }


def has_memory_context(
    context: dict,
) -> bool:
    """
    Check whether athlete has stored memories.
    """

    return bool(
        context.get(
            "memory_context",
        ),
    )
