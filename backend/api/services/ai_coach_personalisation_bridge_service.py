from api.services.personalised_coach_conversation_service import (
    run_personalised_conversation_pipeline,
)


def build_full_personalised_coach_context(
    athlete_id: int,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Build complete personalised coach context.

    Combines:
    - Athlete data
    - Historical performance
    - Recovery patterns
    - Decision analytics
    """

    return {
        "athlete_id": athlete_id,
        "athlete_profile": athlete_profile,
        "training_history": training_history,
        "recovery_history": recovery_history,
        "decision_analysis": decision_analysis,
        "current_state": current_state,
    }


def apply_personalised_strategy(
    coach_response: dict,
    personalised_context: dict,
) -> dict:
    """
    Apply athlete-specific strategy
    to coach response.
    """

    result = run_personalised_conversation_pipeline(
        athlete_id=personalised_context["athlete_id"],
        athlete_profile=personalised_context["athlete_profile"],
        training_history=personalised_context["training_history"],
        recovery_history=personalised_context["recovery_history"],
        decision_analysis=personalised_context["decision_analysis"],
        current_state=personalised_context["current_state"],
        coach_response=coach_response,
    )

    return result


def generate_final_coach_response(
    coach_response: dict,
    personalised_context: dict,
) -> dict:
    """
    Generate final AI Coach response
    using personalised strategy.
    """

    personalised_response = apply_personalised_strategy(
        coach_response=coach_response,
        personalised_context=personalised_context,
    )

    return {
        "coach_response": coach_response,
        "personalised_response": personalised_response,
        "strategy": personalised_response.get(
            "strategy",
            "",
        ),
        "confidence": personalised_response.get(
            "confidence",
            50,
        ),
    }


def run_ai_coach_personalisation_bridge(
    athlete_id: int,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
    coach_response: dict,
) -> dict:
    """
    Complete AI Coach personalisation bridge.

    Flow:

    AI Response
          ↓
    Athlete Strategy
          ↓
    Personalised Response
    """

    context = build_full_personalised_coach_context(
        athlete_id=athlete_id,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return generate_final_coach_response(
        coach_response=coach_response,
        personalised_context=context,
    )
