from api.services.ai_coach_pipeline_integration_service import (
    run_complete_ai_coach_pipeline,
)


def build_response_pipeline_context(
    athlete_id: int,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Build complete response pipeline context.

    Contains all information required
    for final AI Coach output.
    """

    return {
        "athlete_id": athlete_id,
        "athlete_profile": athlete_profile,
        "training_history": training_history,
        "recovery_history": recovery_history,
        "decision_analysis": decision_analysis,
        "current_state": current_state,
    }


def orchestrate_final_coach_response(
    athlete_id: int,
    ai_response: dict,
    pipeline_context: dict,
) -> dict:
    """
    Run final AI Coach response orchestration.

    Flow:

    AI Response
          ↓
    Pipeline Integration
          ↓
    Personalised Strategy
          ↓
    Final Answer
    """

    return run_complete_ai_coach_pipeline(
        athlete_id=athlete_id,
        ai_response=ai_response,
        athlete_profile=pipeline_context["athlete_profile"],
        training_history=pipeline_context["training_history"],
        recovery_history=pipeline_context["recovery_history"],
        decision_analysis=pipeline_context["decision_analysis"],
        current_state=pipeline_context["current_state"],
    )


def generate_production_ai_coach_answer(
    athlete_id: int,
    ai_response: dict,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Generate production AI Coach answer.

    Main output used by API layer.
    """

    context = build_response_pipeline_context(
        athlete_id=athlete_id,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return orchestrate_final_coach_response(
        athlete_id=athlete_id,
        ai_response=ai_response,
        pipeline_context=context,
    )


def run_ai_coach_response_orchestrator(
    athlete_id: int,
    ai_response: dict,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Complete AI Coach response orchestrator.

    Production entry point.
    """

    return generate_production_ai_coach_answer(
        athlete_id=athlete_id,
        ai_response=ai_response,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )
