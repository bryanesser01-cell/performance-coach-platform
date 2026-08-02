from api.services.ai_coach_response_orchestrator_service import (
    run_ai_coach_response_orchestrator,
)


def build_live_conversation_context(
    athlete_id: int,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
    question: str,
) -> dict:
    """
    Build live AI Coach conversation context.

    Includes:
    - Athlete information
    - Training history
    - Recovery history
    - Decision history
    - Current athlete state
    - User question
    """

    return {
        "athlete_id": athlete_id,
        "athlete_profile": athlete_profile,
        "training_history": training_history,
        "recovery_history": recovery_history,
        "decision_analysis": decision_analysis,
        "current_state": current_state,
        "question": question,
    }


def generate_live_personalised_response(
    athlete_id: int,
    ai_response: dict,
    context: dict,
) -> dict:
    """
    Generate final personalised response
    for live conversation.
    """

    return run_ai_coach_response_orchestrator(
        athlete_id=athlete_id,
        ai_response=ai_response,
        athlete_profile=context["athlete_profile"],
        training_history=context["training_history"],
        recovery_history=context["recovery_history"],
        decision_analysis=context["decision_analysis"],
        current_state=context["current_state"],
    )


def process_live_coach_question(
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
    Process a live AI Coach question.

    Flow:

    Athlete Question
          ↓
    Context Builder
          ↓
    AI Response
          ↓
    Personalisation
          ↓
    Final Answer
    """

    context = build_live_conversation_context(
        athlete_id=athlete_id,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
        question=question,
    )

    response = generate_live_personalised_response(
        athlete_id=athlete_id,
        ai_response=ai_response,
        context=context,
    )

    return {
        "athlete_id": athlete_id,
        "question": question,
        "response": response,
    }


def run_live_ai_coach_pipeline(
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
    Production live AI Coach entry point.
    """

    return process_live_coach_question(
        athlete_id=athlete_id,
        question=question,
        ai_response=ai_response,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )
