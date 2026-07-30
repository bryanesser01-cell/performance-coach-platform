from api.services.ai_coach_learning_pipeline_service import (
    run_learning_pipeline,
)


def apply_learning_to_response(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Apply learning pipeline and return
    the learning result only.
    """

    pipeline_result = run_learning_pipeline(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )

    return pipeline_result[
        "learning_result"
    ]


def enrich_response_with_learning(
    response: dict,
    learning_result: dict,
) -> dict:
    """
    Attach learning information to
    the final coach response.
    """

    return {
        **response,
        "learning_updated": True,
        "learning_result": learning_result,
    }


def finalise_ai_coach_response(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Complete final AI Coach response flow.

    Flow:

    AI Coach Response
          ↓
    Learning Pipeline
          ↓
    Attach Learning
    """

    learning_result = apply_learning_to_response(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )

    return enrich_response_with_learning(
        response=response,
        learning_result=learning_result,
    )
