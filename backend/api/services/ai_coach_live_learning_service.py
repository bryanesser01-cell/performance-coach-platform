from api.services.ai_coach_learning_orchestrator_service import (
    complete_coach_interaction,
)


def process_live_coach_response(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Process a live AI Coach response.

    Flow:

    Live API Response
          ↓
    Learning Orchestrator
          ↓
    Learning Context Added
    """

    return complete_coach_interaction(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def apply_live_learning(
    response: dict,
    learning_response: dict,
) -> dict:
    """
    Apply learning data to live response.
    """

    return {
        **response,
        "learning_applied": True,
        "learning_context": (
            learning_response.get(
                "learning_context",
                {},
            )
        ),
    }


def build_final_coach_output(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Build final live AI Coach output.

    Flow:

    AI Coach Response
          ↓
    Live Learning Service
          ↓
    Final Output
    """

    learning_response = process_live_coach_response(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )

    return apply_live_learning(
        response=response,
        learning_response=learning_response,
    )
