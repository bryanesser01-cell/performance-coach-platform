from api.services.ai_coach_live_service_router import (
    run_live_service_router,
)


def create_conversation_entry(
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
    Create the final conversation entry request.

    This is the single entry preparation layer
    before the AI Coach brain executes.
    """

    return {
        "athlete_id": athlete_id,
        "question": question,
        "ai_response": ai_response,
        "athlete_profile": athlete_profile,
        "training_history": training_history,
        "recovery_history": recovery_history,
        "decision_analysis": decision_analysis,
        "current_state": current_state,
    }


def execute_conversation_entry(
    entry_request: dict,
) -> dict:
    """
    Execute final AI Coach entry path.

    Flow:

    Conversation Entry
            ↓
    Live Router
            ↓
    Production Controller
            ↓
    AI Coach Brain
            ↓
    Athlete Response
    """

    return run_live_service_router(
        athlete_id=entry_request["athlete_id"],
        question=entry_request["question"],
        ai_response=entry_request["ai_response"],
        athlete_profile=entry_request["athlete_profile"],
        training_history=entry_request["training_history"],
        recovery_history=entry_request["recovery_history"],
        decision_analysis=entry_request["decision_analysis"],
        current_state=entry_request["current_state"],
    )


def run_ai_coach_entry(
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
    Final AI Coach production entry point.

    Production flow:

    User Question
          ↓
    AI Coach Entry
          ↓
    Full AI Coach Brain
          ↓
    Personalised Answer
    """

    request = create_conversation_entry(
        athlete_id=athlete_id,
        question=question,
        ai_response=ai_response,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return execute_conversation_entry(
        request,
    )
