from api.services.ai_coach_live_route_service import (
    handle_chat_route,
    handle_conversation_route,
)


def cutover_conversation_endpoint(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Cut over conversation endpoint
    to the new AI Coach architecture.

    Flow:

    Endpoint
       ↓
    Live Route Service
       ↓
    Learning Pipeline
       ↓
    Final Response
    """

    return handle_conversation_route(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def cutover_chat_endpoint(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Cut over chat endpoint
    to the new AI Coach architecture.
    """

    return handle_chat_route(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def verify_endpoint_contract(
    response: dict,
) -> dict:
    """
    Verify public endpoint response contract.
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
