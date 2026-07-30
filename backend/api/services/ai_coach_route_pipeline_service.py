from api.services.ai_coach_response_pipeline_service import (
    finalise_live_response,
)


def process_conversation_request(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Process AI Coach conversation request.

    Flow:

    Conversation Request
          ↓
    Response Pipeline
          ↓
    Learning
          ↓
    Final Response
    """

    return finalise_live_response(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def process_chat_request(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Process athlete chat request.

    Uses the same production pipeline
    as conversation requests.
    """

    return finalise_live_response(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def build_route_response(
    response: dict,
) -> dict:
    """
    Build final API route response.
    """

    return {
        "success": True,
        "data": response,
    }
