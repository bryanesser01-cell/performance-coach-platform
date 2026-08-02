from api.services.athlete_strategy_integration_service import (
    run_personalised_strategy_pipeline,
)


def build_personalised_conversation_context(
    athlete_id: int,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Build personalised conversation context.

    Uses:
    - Athlete profile
    - Training history
    - Recovery history
    - Decision analytics
    """

    strategy_context = run_personalised_strategy_pipeline(
        athlete_id=athlete_id,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
        decision={
            "decision": ("MAINTAIN_TRAINING"),
        },
    )

    return {
        "athlete_id": athlete_id,
        "strategy_context": strategy_context,
    }


def merge_strategy_with_coach_response(
    coach_response: dict,
    personalised_context: dict,
) -> dict:
    """
    Attach personalised strategy
    to coach response.
    """

    strategy_context = personalised_context.get(
        "strategy_context",
        {},
    )

    return {
        **coach_response,
        "personalised_strategy": (
            strategy_context.get(
                "strategy",
                "",
            )
        ),
        "strategy_confidence": (
            strategy_context.get(
                "confidence",
                50,
            )
        ),
    }


def generate_personalised_training_advice(
    personalised_response: dict,
) -> dict:
    """
    Generate final athlete advice.
    """

    strategy = personalised_response.get(
        "personalised_strategy",
        "BALANCED_TRAINING",
    )

    confidence = personalised_response.get(
        "strategy_confidence",
        50,
    )

    return {
        "advice": (
            "Your training recommendation "
            "has been personalised from "
            "your previous responses."
        ),
        "strategy": strategy,
        "confidence": confidence,
    }


def run_personalised_conversation_pipeline(
    athlete_id: int,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
    coach_response: dict,
) -> dict:
    """
    Complete personalised conversation pipeline.

    Flow:

    Athlete Data
          ↓
    Strategy Engine
          ↓
    Coach Response
          ↓
    Personalised Advice
    """

    context = build_personalised_conversation_context(
        athlete_id=athlete_id,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    merged_response = merge_strategy_with_coach_response(
        coach_response=coach_response,
        personalised_context=context,
    )

    return generate_personalised_training_advice(
        merged_response,
    )
