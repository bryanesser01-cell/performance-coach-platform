from api.services.ai_coach_production_cutover_service import (
    activate_production_chat_route,
    activate_production_conversation_route,
)


def simplify_conversation_route(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Simplified conversation route.

    New architecture:

    Route
      ↓
    Production Pipeline
      ↓
    Learning System
      ↓
    Response
    """

    return activate_production_conversation_route(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def simplify_chat_route(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Simplified chat route.

    Uses the same production pipeline.
    """

    return activate_production_chat_route(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def verify_route_architecture(
    response: dict,
) -> dict:
    """
    Verify simplified route architecture.
    """

    return {
        "architecture_valid": (
            response.get(
                "success",
                False,
            )
            and "data" in response
        ),
        "response": response,
    }
