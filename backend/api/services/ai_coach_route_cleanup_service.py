from api.services.ai_coach_endpoint_router_service import (
    route_chat_request,
    route_conversation_request,
)


def cleanup_conversation_route(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Replace legacy conversation route logic.

    Old:

    Route
      ↓
    Controller
      ↓
    Formatter
      ↓
    Response

    New:

    Route
      ↓
    Endpoint Router
      ↓
    AI Coach Pipeline
      ↓
    Response
    """

    return route_conversation_request(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def cleanup_chat_route(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Replace legacy chat route logic.

    Uses the unified AI Coach pipeline.
    """

    return route_chat_request(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def verify_no_legacy_path(
    route_response: dict,
) -> dict:
    """
    Verify route uses the new pipeline.

    Legacy routes should return the
    standard response contract.
    """

    return {
        "legacy_removed": (
            route_response.get(
                "success",
                False,
            )
            and "data" in route_response
        ),
        "response": route_response,
    }
