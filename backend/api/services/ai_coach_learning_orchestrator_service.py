from api.services.ai_coach_response_learning_service import (
    finalise_ai_coach_response,
)


def orchestrate_learning_after_response(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Trigger learning after an AI Coach response.

    Flow:

    AI Coach Response
          ↓
    Learning Service
          ↓
    Learning Memory Update
    """

    return finalise_ai_coach_response(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def attach_learning_context(
    response: dict,
    learning_response: dict,
) -> dict:
    """
    Attach learning context to final response.
    """

    return {
        **response,
        "learning_context": {
            "learning_updated": (
                learning_response.get(
                    "learning_updated",
                    False,
                )
            ),
            "learning_result": (
                learning_response.get(
                    "learning_result",
                    {},
                )
            ),
        },
    }


def complete_coach_interaction(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Complete AI Coach interaction lifecycle.

    Flow:

    Coach Response
          ↓
    Learning Orchestration
          ↓
    Attach Learning Context
          ↓
    Final Response
    """

    learning_response = orchestrate_learning_after_response(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )

    return attach_learning_context(
        response=response,
        learning_response=learning_response,
    )
