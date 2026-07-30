from api.services.ai_coach_route_simplification_service import (
    simplify_chat_route,
    simplify_conversation_route,
)


def process_ai_coach_request(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Core AI Coach processing boundary.

    Flow:

    Request
      ↓
    AI Coach Core
      ↓
    Production Pipeline
      ↓
    Learning System
      ↓
    Response
    """

    return simplify_conversation_route(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def process_ai_coach_conversation(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Process AI Coach conversation requests.
    """

    return simplify_conversation_route(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def process_ai_coach_chat(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Process AI Coach chat requests.
    """

    return simplify_chat_route(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )
