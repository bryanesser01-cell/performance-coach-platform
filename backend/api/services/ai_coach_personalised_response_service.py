from api.services.ai_coach_personalisation_bridge_service import (
    run_ai_coach_personalisation_bridge,
)


def build_personalised_response_context(
    athlete_id: int,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Build complete personalised response context.

    Includes:
    - Athlete profile
    - Training history
    - Recovery history
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


def apply_athlete_strategy(
    coach_response: dict,
    personalised_context: dict,
) -> dict:
    """
    Apply athlete-specific strategy
    to AI Coach response.
    """

    result = run_ai_coach_personalisation_bridge(
        athlete_id=personalised_context[
            "athlete_id"
        ],
        athlete_profile=personalised_context[
            "athlete_profile"
        ],
        training_history=personalised_context[
            "training_history"
        ],
        recovery_history=personalised_context[
            "recovery_history"
        ],
        decision_analysis=personalised_context[
            "decision_analysis"
        ],
        current_state=personalised_context[
            "current_state"
        ],
        coach_response=coach_response,
    )

    return result


def generate_final_personalised_answer(
    coach_response: dict,
    personalised_context: dict,
) -> dict:
    """
    Generate final AI Coach answer.

    Adds:
    - Strategy
    - Confidence
    - Personalised message
    """

    personalised_result = apply_athlete_strategy(
        coach_response=coach_response,
        personalised_context=personalised_context,
    )

    return {
        "answer": (
            personalised_result
            .get(
                "personalised_response",
                {},
            )
            .get(
                "advice",
                "Your training has been personalised.",
            )
        ),
        "strategy": personalised_result.get(
            "strategy",
            "",
        ),
        "confidence": personalised_result.get(
            "confidence",
            50,
        ),
        "coach_response": coach_response,
    }


def run_personalised_response_pipeline(
    athlete_id: int,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
    coach_response: dict,
) -> dict:
    """
    Complete personalised response pipeline.

    Flow:

    Coach Response
          ↓
    Athlete Strategy
          ↓
    Final Personalised Answer
    """

    context = build_personalised_response_context(
        athlete_id=athlete_id,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return generate_final_personalised_answer(
        coach_response=coach_response,
        personalised_context=context,
    )
