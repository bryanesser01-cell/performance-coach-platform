from api.services.ai_coach_endpoint_cutover_service import (
    cutover_chat_endpoint,
    cutover_conversation_endpoint,
)


def route_conversation_request(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Route conversation endpoint request.

    Flow:

    FastAPI Endpoint
          ↓
    Endpoint Router Service
          ↓
    Endpoint Cutover
          ↓
    AI Coach Pipeline
          ↓
    Response
    """

    return cutover_conversation_endpoint(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def route_chat_request(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Route chat endpoint request.

    Uses the same production pipeline.
    """

    return cutover_chat_endpoint(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def normalise_endpoint_response(
    response: dict,
) -> dict:
    """
    Normalise endpoint output.

    Ensures the public API contract
    remains consistent.
    """

    return {
        "success": response.get(
            "success",
            False,
        ),
        "data": response.get(
            "data",
            {},
        ),
    }
