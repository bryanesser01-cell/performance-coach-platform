from api.services.athlete_strategy_engine_service import (
    run_athlete_strategy_engine,
)


def build_personalised_coach_context(
    athlete_id: int,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Build personalised AI Coach context.

    Combines:
    - Athlete profile
    - Training history
    - Recovery patterns
    - Decision analytics
    """

    strategy = run_athlete_strategy_engine(
        athlete_id=athlete_id,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return {
        "athlete_id": athlete_id,
        "personalised_strategy": strategy,
    }


def apply_strategy_to_decision(
    decision: dict,
    personalised_context: dict,
) -> dict:
    """
    Adjust AI decision using athlete strategy.
    """

    strategy = personalised_context.get(
        "personalised_strategy",
        {},
    )

    recommended_strategy = strategy.get(
        "recommended_strategy",
        "",
    )

    return {
        **decision,
        "athlete_strategy": recommended_strategy,
        "strategy_confidence": strategy.get(
            "confidence",
            50,
        ),
    }


def generate_personalised_coach_response(
    decision: dict,
) -> dict:
    """
    Generate athlete-specific coaching response.
    """

    strategy = decision.get(
        "athlete_strategy",
        "BALANCED_TRAINING",
    )

    confidence = decision.get(
        "strategy_confidence",
        50,
    )

    return {
        "decision": decision.get(
            "decision",
            "",
        ),
        "strategy": strategy,
        "confidence": confidence,
        "message": (
            "Your recommendation has been "
            "personalised using your training "
            "history and previous responses."
        ),
    }


def run_personalised_strategy_pipeline(
    athlete_id: int,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
    decision: dict,
) -> dict:
    """
    Complete personalised strategy pipeline.

    Flow:

    Athlete Data
          ↓
    Strategy Engine
          ↓
    Decision Adjustment
          ↓
    Personalised Response
    """

    context = build_personalised_coach_context(
        athlete_id=athlete_id,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    updated_decision = apply_strategy_to_decision(
        decision=decision,
        personalised_context=context,
    )

    return generate_personalised_coach_response(
        updated_decision,
    )
