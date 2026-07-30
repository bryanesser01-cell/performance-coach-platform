from api.services.ai_coach_conversation_orchestrator_service import (
    orchestrate_coach_conversation,
)


def integrate_ai_coach_pipeline(
    athlete_id: int,
    ai_response: dict,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Connect AI Coach response to the
    complete personalisation pipeline.

    Flow:

    AI Response
          ↓
    Orchestrator
          ↓
    Strategy Engine
          ↓
    Personalised Response
    """

    return orchestrate_coach_conversation(
        athlete_id=athlete_id,
        ai_response=ai_response,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )


def build_production_coach_response(
    pipeline_result: dict,
) -> dict:
    """
    Build final production response.

    Keeps API response clean.
    """

    return {
        "answer": pipeline_result.get(
            "answer",
            "",
        ),
        "strategy": pipeline_result.get(
            "strategy",
            "",
        ),
        "confidence": pipeline_result.get(
            "confidence",
            50,
        ),
    }


def run_complete_ai_coach_pipeline(
    athlete_id: int,
    ai_response: dict,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Complete production AI Coach pipeline.

    Flow:

    Athlete
       ↓
    AI Response
       ↓
    Personalisation
       ↓
    Final Coach Output
    """

    result = integrate_ai_coach_pipeline(
        athlete_id=athlete_id,
        ai_response=ai_response,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return build_production_coach_response(
        result,
    )
