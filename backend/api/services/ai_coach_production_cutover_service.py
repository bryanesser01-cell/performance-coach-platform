from api.services.ai_coach_route_cleanup_service import (
    cleanup_chat_route,
    cleanup_conversation_route,
)


def activate_production_conversation_route(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Activate production conversation route.

    Final production flow:

    FastAPI
       ↓
    Production Cutover
       ↓
    AI Coach Pipeline
       ↓
    Learning System
       ↓
    Response
    """

    return cleanup_conversation_route(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def activate_production_chat_route(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Activate production chat route.
    """

    return cleanup_chat_route(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def verify_production_pipeline(
    response: dict,
) -> dict:
    """
    Verify production response uses
    the new AI Coach pipeline.
    """

    return {
        "production_ready": (
            response.get(
                "success",
                False,
            )
            and "data" in response
            and response["data"].get(
                "learning_applied",
                False,
            )
        ),
        "response": response,
    }
