from api.services.ai_coach_route_adapter_service import (
    adapt_chat_route,
    adapt_conversation_route,
)


def migrate_conversation_route(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Migrate conversation route to the
    new AI Coach pipeline.

    Old:

    Route
      ↓
    Controller
      ↓
    Response

    New:

    Route
      ↓
    Adapter
      ↓
    Pipeline
      ↓
    Learning
      ↓
    Response
    """

    return adapt_conversation_route(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def migrate_chat_route(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Migrate chat route to the
    new AI Coach pipeline.
    """

    return adapt_chat_route(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def validate_route_migration(
    result: dict,
) -> dict:
    """
    Validate migrated route response.
    """

    return {
        "valid": (
            result.get(
                "success",
                False,
            )
            and "data" in result
        ),
        "response": result,
    }
