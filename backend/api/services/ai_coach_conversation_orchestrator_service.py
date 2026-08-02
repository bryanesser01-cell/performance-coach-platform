from api.services.ai_coach_final_response_service import (
    run_final_coach_response_pipeline,
)


def build_complete_ai_coach_pipeline(
    athlete_id: int,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Build complete AI Coach pipeline context.

    Includes:
    - Athlete profile
    - Training history
    - Recovery history
    - Decision analytics
    - Current state
    """

    return {
        "athlete_id": athlete_id,
        "athlete_profile": athlete_profile,
        "training_history": training_history,
        "recovery_history": recovery_history,
        "decision_analysis": decision_analysis,
        "current_state": current_state,
    }


def generate_final_athlete_response(
    athlete_id: int,
    ai_response: dict,
    pipeline_context: dict,
) -> dict:
    """
    Generate final production athlete response.
    """

    return run_final_coach_response_pipeline(
        athlete_id=athlete_id,
        ai_response=ai_response,
        athlete_profile=pipeline_context["athlete_profile"],
        training_history=pipeline_context["training_history"],
        recovery_history=pipeline_context["recovery_history"],
        decision_analysis=pipeline_context["decision_analysis"],
        current_state=pipeline_context["current_state"],
    )


def orchestrate_coach_conversation(
    athlete_id: int,
    ai_response: dict,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Main AI Coach orchestration layer.

    Flow:

    Athlete Data
          ↓
    Context Builder
          ↓
    AI Response
          ↓
    Personalisation
          ↓
    Final Athlete Response
    """

    context = build_complete_ai_coach_pipeline(
        athlete_id=athlete_id,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return generate_final_athlete_response(
        athlete_id=athlete_id,
        ai_response=ai_response,
        pipeline_context=context,
    )
