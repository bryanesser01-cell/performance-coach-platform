from api.services.ai_coach_production_controller_service import (
    run_production_controller,
)


def build_live_service_request(
    athlete_id: int,
    question: str,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Build live service request.

    Entry layer between:
    - API conversation service
    - Production AI Coach controller
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


def generate_live_service_response(
    request: dict,
    ai_response: dict,
) -> dict:
    """
    Generate live AI Coach response.

    Routes request into the complete
    production AI Coach brain.
    """

    return run_production_controller(
        athlete_id=request["athlete_id"],
        question=request["question"],
        ai_response=ai_response,
        athlete_profile=request["athlete_profile"],
        training_history=request["training_history"],
        recovery_history=request["recovery_history"],
        decision_analysis=request["decision_analysis"],
        current_state=request["current_state"],
    )


def route_live_ai_coach_request(
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
    Main live AI Coach router.

    Flow:

    User Question
          ↓
    Live Router
          ↓
    Production Controller
          ↓
    Full AI Coach Brain
          ↓
    Personalised Response
    """

    request = build_live_service_request(
        athlete_id=athlete_id,
        question=question,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return generate_live_service_response(
        request=request,
        ai_response=ai_response,
    )


def run_live_service_router(
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
    Production live service entry point.
    """

    return route_live_ai_coach_request(
        athlete_id=athlete_id,
        question=question,
        ai_response=ai_response,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )
