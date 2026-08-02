from api.services.ai_coach_conversation_production_bridge_service import (
    run_production_conversation_bridge,
)


def build_runtime_context(
    athlete_id: int,
    question: str,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Build runtime conversation context.

    This is the final context layer before
    production AI Coach execution.
    """

    return {
        "athlete_id": athlete_id,
        "question": question,
        "athlete_profile": athlete_profile,
        "training_history": training_history,
        "recovery_history": recovery_history,
        "decision_analysis": decision_analysis,
        "current_state": current_state,
    }


def execute_runtime_conversation(
    runtime_context: dict,
    ai_response: dict,
) -> dict:
    """
    Execute complete production conversation.

    Flow:

    Runtime Context
          ↓
    Production Bridge
          ↓
    AI Coach Brain
          ↓
    Personalised Answer
    """

    return run_production_conversation_bridge(
        athlete_id=runtime_context["athlete_id"],
        question=runtime_context["question"],
        ai_response=ai_response,
        athlete_profile=runtime_context["athlete_profile"],
        training_history=runtime_context["training_history"],
        recovery_history=runtime_context["recovery_history"],
        decision_analysis=runtime_context["decision_analysis"],
        current_state=runtime_context["current_state"],
    )


def generate_runtime_response(
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
    Generate production runtime response.

    This becomes the final conversation
    execution layer.
    """

    context = build_runtime_context(
        athlete_id=athlete_id,
        question=question,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return execute_runtime_conversation(
        runtime_context=context,
        ai_response=ai_response,
    )


def run_ai_coach_runtime(
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
    Main runtime AI Coach entry point.
    """

    return generate_runtime_response(
        athlete_id=athlete_id,
        question=question,
        ai_response=ai_response,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )
