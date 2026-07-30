from api.services.ai_coach_route_migration_service import (
    migrate_chat_route,
    migrate_conversation_route,
)


def execute_conversation_cutover(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Execute conversation route through
    the new AI Coach architecture.

    Flow:

    Conversation Route
          ↓
    Migration Service
          ↓
    Pipeline
          ↓
    Learning
          ↓
    Response
    """

    return migrate_conversation_route(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def execute_chat_cutover(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Execute chat route through
    the new AI Coach architecture.
    """

    return migrate_chat_route(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def verify_cutover_response(
    response: dict,
) -> dict:
    """
    Verify migrated response contract.
    """

    return {
        "cutover_successful": (
            response.get(
                "success",
                False,
            )
            and "data" in response
        ),
        "response": response,
    }
