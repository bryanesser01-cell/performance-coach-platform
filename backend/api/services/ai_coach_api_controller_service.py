from api.services.ai_coach_conversation_entry_service import (
    run_ai_coach_entry,
)


def prepare_api_coach_request(
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
    Prepare API request for AI Coach execution.

    This is the API-facing preparation layer.
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


def execute_api_coach_request(
    request: dict,
) -> dict:
    """
    Execute API request through the
    complete AI Coach brain.

    Flow:

    API
      ↓
    Entry Service
      ↓
    AI Coach Brain
      ↓
    Response
    """

    return run_ai_coach_entry(
        athlete_id=request["athlete_id"],
        question=request["question"],
        ai_response=request["ai_response"],
        athlete_profile=request["athlete_profile"],
        training_history=request["training_history"],
        recovery_history=request["recovery_history"],
        decision_analysis=request["decision_analysis"],
        current_state=request["current_state"],
    )


def generate_api_coach_response(
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
    Generate final API AI Coach response.
    """

    request = prepare_api_coach_request(
        athlete_id=athlete_id,
        question=question,
        ai_response=ai_response,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return execute_api_coach_request(
        request,
    )


def run_api_coach_controller(
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
    Main API controller entry point.

    Production flow:

    API Request
          ↓
    AI Coach Controller
          ↓
    Full AI Coach Brain
          ↓
    Personalised Response
    """

    return generate_api_coach_response(
        athlete_id=athlete_id,
        question=question,
        ai_response=ai_response,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )
