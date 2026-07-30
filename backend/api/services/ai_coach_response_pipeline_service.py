from api.services.ai_coach_live_learning_service import (
    build_final_coach_output,
)


def run_coach_response_pipeline(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Run the complete AI Coach response pipeline.

    Flow:

    AI Coach Response
          ↓
    Live Learning Service
          ↓
    Learning Update
          ↓
    Final Response
    """

    return build_final_coach_output(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )


def apply_response_learning(
    response: dict,
    learning_response: dict,
) -> dict:
    """
    Apply learning metadata to response.
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


def finalise_live_response(
    athlete_id: int,
    question: str,
    response: dict,
) -> dict:
    """
    Build final production AI Coach response.

    Flow:

    Response
       ↓
    Learning Pipeline
       ↓
    Final API Output
    """

    pipeline_response = run_coach_response_pipeline(
        athlete_id=athlete_id,
        question=question,
        response=response,
    )

    return apply_response_learning(
        response=response,
        learning_response=pipeline_response,
    )
