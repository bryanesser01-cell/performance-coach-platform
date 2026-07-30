from api.services.ai_coach_production_cutover_service import (
    activate_production_chat_route,
    activate_production_conversation_route,
)


def remove_legacy_controller_path(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Remove legacy controller path.

    Old:

    Route
      ↓
    Controller
      ↓
    Formatter

    New:

    Route
      ↓
    Production Pipeline
      ↓
    Learning AI Coach
    """

    return activate_production_conversation_route(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def remove_legacy_formatter_path(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Remove legacy formatter path.

    Uses the unified production pipeline.
    """

    return activate_production_chat_route(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def verify_single_pipeline(
    response: dict,
) -> dict:
    """
    Verify only the production pipeline
    is active.
    """

    return {
        "single_pipeline_active": (
            response.get(
                "success",
                False,
            )
            and "data" in response
        ),
        "response": response,
    }
