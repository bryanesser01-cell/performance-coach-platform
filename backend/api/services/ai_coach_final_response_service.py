from api.services.ai_coach_personalised_response_service import (
    run_personalised_response_pipeline,
)


def build_final_coach_context(
    athlete_id: int,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
    coach_context: dict | None = None,
) -> dict:
    """
    Build final AI Coach context.

    Combines:
    - Athlete information
    - Training history
    - Recovery history
    - Decision analytics
    - Existing coach context
    """

    return {
        "athlete_id": athlete_id,
        "athlete_profile": athlete_profile,
        "training_history": training_history,
        "recovery_history": recovery_history,
        "decision_analysis": decision_analysis,
        "current_state": current_state,
        "coach_context": coach_context or {},
    }


def combine_ai_and_personalised_response(
    ai_response: dict,
    personalised_response: dict,
) -> dict:
    """
    Merge standard AI response with
    personalised strategy output.
    """

    return {
        "coach_message": ai_response.get(
            "coach_message",
            "",
        ),
        "personalised_answer": personalised_response.get(
            "answer",
            "",
        ),
        "strategy": personalised_response.get(
            "strategy",
            "",
        ),
        "confidence": personalised_response.get(
            "confidence",
            50,
        ),
    }


def generate_final_ai_coach_answer(
    athlete_id: int,
    ai_response: dict,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
    coach_context: dict | None = None,
) -> dict:
    """
    Generate final production AI Coach response.

    Flow:

    AI Response
          ↓
    Personalised Engine
          ↓
    Final Answer
    """

    personalised_response = run_personalised_response_pipeline(
        athlete_id=athlete_id,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
        coach_response=ai_response,
    )

    return combine_ai_and_personalised_response(
        ai_response=ai_response,
        personalised_response=personalised_response,
    )


def run_final_coach_response_pipeline(
    athlete_id: int,
    ai_response: dict,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Complete final AI Coach pipeline.
    """

    context = build_final_coach_context(
        athlete_id=athlete_id,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return generate_final_ai_coach_answer(
        athlete_id=context["athlete_id"],
        ai_response=ai_response,
        athlete_profile=context["athlete_profile"],
        training_history=context["training_history"],
        recovery_history=context["recovery_history"],
        decision_analysis=context["decision_analysis"],
        current_state=context["current_state"],
        coach_context=context["coach_context"],
    )
