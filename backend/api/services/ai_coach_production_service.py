from api.services.ai_coach_live_conversation_service import (
    run_live_ai_coach_pipeline,
)


def build_production_context(
    athlete_id: int,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Build complete production AI Coach context.

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


def generate_production_answer(
    athlete_id: int,
    question: str,
    ai_response: dict,
    production_context: dict,
) -> dict:
    """
    Generate final production AI Coach answer.

    Uses full AI Coach pipeline.
    """

    return run_live_ai_coach_pipeline(
        athlete_id=athlete_id,
        question=question,
        ai_response=ai_response,
        athlete_profile=production_context["athlete_profile"],
        training_history=production_context["training_history"],
        recovery_history=production_context["recovery_history"],
        decision_analysis=production_context["decision_analysis"],
        current_state=production_context["current_state"],
    )


def run_production_coach(
    athlete_id: int,
    question: str,
    ai_response: dict,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Main production AI Coach entry point.

    Flow:

    Athlete Question
          ↓
    Full AI Brain
          ↓
    Personalised Answer
    """

    context = build_production_context(
        athlete_id=athlete_id,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return generate_production_answer(
        athlete_id=athlete_id,
        question=question,
        ai_response=ai_response,
        production_context=context,
    )
