from api.services.ai_coach_conversation_final_service import (
    run_final_conversation_service,
)


def build_controller_request(
    athlete_id: int,
    question: str,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Build production controller request.

    Final controller layer between:
    - Conversation API
    - AI Coach Brain
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


def execute_production_controller(
    request: dict,
    ai_response: dict,
) -> dict:
    """
    Execute final AI Coach production flow.

    Flow:

    API Request
        ↓
    Controller
        ↓
    Final Conversation Service
        ↓
    AI Coach Brain
        ↓
    Athlete Response
    """

    return run_final_conversation_service(
        athlete_id=request[
            "athlete_id"
        ],
        question=request[
            "question"
        ],
        ai_response=ai_response,
        athlete_profile=request[
            "athlete_profile"
        ],
        training_history=request[
            "training_history"
        ],
        recovery_history=request[
            "recovery_history"
        ],
        decision_analysis=request[
            "decision_analysis"
        ],
        current_state=request[
            "current_state"
        ],
    )


def generate_controller_response(
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
    Generate final production AI Coach response.
    """

    request = build_controller_request(
        athlete_id=athlete_id,
        question=question,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return execute_production_controller(
        request=request,
        ai_response=ai_response,
    )


def run_production_controller(
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
    Main production controller entry point.

    Final architecture:

    User
      ↓
    Controller
      ↓
    AI Coach Brain
      ↓
    Personalised Answer
    """

    return generate_controller_response(
        athlete_id=athlete_id,
        question=question,
        ai_response=ai_response,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )
