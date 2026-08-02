from api.services.ai_coach_conversation_runtime_service import (
    run_ai_coach_runtime,
)


def build_cutover_request(
    athlete_id: int,
    question: str,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Build new production conversation request.

    This replaces the old static conversation path.
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


def execute_new_conversation_path(
    request: dict,
    ai_response: dict,
) -> dict:
    """
    Execute the complete AI Coach brain.

    Flow:

    Conversation Service
            ↓
    Runtime Service
            ↓
    Full AI Coach Pipeline
            ↓
    Personalised Answer
    """

    return run_ai_coach_runtime(
        athlete_id=request["athlete_id"],
        question=request["question"],
        ai_response=ai_response,
        athlete_profile=request["athlete_profile"],
        training_history=request["training_history"],
        recovery_history=request["recovery_history"],
        decision_analysis=request["decision_analysis"],
        current_state=request["current_state"],
    )


def generate_cutover_response(
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
    Generate final production response
    through the new AI Coach path.
    """

    request = build_cutover_request(
        athlete_id=athlete_id,
        question=question,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return execute_new_conversation_path(
        request=request,
        ai_response=ai_response,
    )


def run_conversation_cutover(
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
    Main cutover entry point.

    Production path:

    Question
        ↓
    AI Coach Brain
        ↓
    Personalised Answer
    """

    return generate_cutover_response(
        athlete_id=athlete_id,
        question=question,
        ai_response=ai_response,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )
