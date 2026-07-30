from api.services.ai_coach_route_pipeline_service import (
    build_route_response,
    process_chat_request,
    process_conversation_request,
)


def prepare_route_context(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Prepare common route context.

    Shared by conversation and chat routes.
    """

    return {
        "athlete_id": athlete_id,
        "question": question,
        "response": response,
    }


def adapt_conversation_route(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Adapt /ai-coach/conversation route.

    Flow:

    Route
      ↓
    Adapter
      ↓
    Route Pipeline
      ↓
    API Response
    """

    context = prepare_route_context(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )

    pipeline_response = process_conversation_request(
        athlete_id=context["athlete_id"],
        question=context["question"],
        response=context["response"],
    )

    return build_route_response(
        pipeline_response,
    )


def adapt_chat_route(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Adapt athlete chat route.

    Uses the same pipeline as conversation.
    """

    context = prepare_route_context(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )

    pipeline_response = process_chat_request(
        athlete_id=context["athlete_id"],
        question=context["question"],
        response=context["response"],
    )

    return build_route_response(
        pipeline_response,
    )
