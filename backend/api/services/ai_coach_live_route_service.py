from api.services.ai_coach_route_cutover_service import (
    execute_chat_cutover,
    execute_conversation_cutover,
)


def handle_conversation_route(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Handle live conversation route.

    Flow:

    FastAPI Route
          ↓
    Cutover Service
          ↓
    AI Coach Pipeline
          ↓
    Learning
          ↓
    Response
    """

    return execute_conversation_cutover(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def handle_chat_route(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Handle live athlete chat route.
    """

    return execute_chat_cutover(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def validate_live_route_response(
    response: dict,
) -> dict:
    """
    Validate final live route response.
    """

    return {
        "valid": (
            response.get(
                "success",
                False,
            )
            and "data" in response
        ),
        "response": response,
    }
