from api.services.ai_coach_production_service import (
    run_production_coach,
)


def build_gateway_context(
    athlete_id: int,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
    question: str,
) -> dict:
    """
    Build conversation gateway context.

    This is the entry layer before
    the complete AI Coach brain.
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


def generate_gateway_response(
    gateway_context: dict,
    ai_response: dict,
) -> dict:
    """
    Generate final response through
    production AI Coach service.
    """

    return run_production_coach(
        athlete_id=gateway_context[
            "athlete_id"
        ],
        question=gateway_context[
            "question"
        ],
        ai_response=ai_response,
        athlete_profile=gateway_context[
            "athlete_profile"
        ],
        training_history=gateway_context[
            "training_history"
        ],
        recovery_history=gateway_context[
            "recovery_history"
        ],
        decision_analysis=gateway_context[
            "decision_analysis"
        ],
        current_state=gateway_context[
            "current_state"
        ],
    )


def route_conversation_request(
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
    Main conversation gateway.

    Flow:

    User Question
          ↓
    Gateway
          ↓
    Production AI Coach
          ↓
    Personalised Answer
    """

    context = build_gateway_context(
        athlete_id=athlete_id,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
        question=question,
    )

    return generate_gateway_response(
        gateway_context=context,
        ai_response=ai_response,
    )


def run_conversation_gateway(
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
    Production conversation gateway entry point.
    """

    return route_conversation_request(
        athlete_id=athlete_id,
        question=question,
        ai_response=ai_response,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )
