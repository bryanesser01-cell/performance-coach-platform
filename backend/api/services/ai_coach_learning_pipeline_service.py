from api.services.ai_coach_learning_integration_service import (
    integrate_coach_learning,
)


def trigger_learning_from_response(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Trigger learning from completed AI Coach response.
    """

    return integrate_coach_learning(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def process_completed_coaching_event(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Process completed coaching interaction.
    """

    learning_result = trigger_learning_from_response(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )

    return {
        "athlete_id": athlete_id,
        "question": question,
        "learning_result": learning_result,
    }


def build_learning_enriched_response(
    response: dict,
    learning_result: dict,
) -> dict:
    """
    Add learning information to response.
    """

    return {
        **response,
        "learning_updated": True,
        "learning_result": learning_result,
    }


def run_learning_pipeline(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Complete AI Coach learning pipeline.

    Flow:

    AI Coach Response
          ↓
    Learning Trigger
          ↓
    Process Event
          ↓
    Learning Enriched Response
    """

    learning_result = trigger_learning_from_response(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )

    return {
        **response,
        "learning_updated": True,
        "learning_result": learning_result,
    }
