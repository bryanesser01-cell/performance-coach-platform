from api.services.ai_coach_conversation_adapter_service import (
    run_adapted_conversation,
)


def build_production_conversation_request(
    athlete_id: int,
    question: str,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Build production conversation request.

    This is the bridge between:
    - Conversation Service
    - Full AI Coach Brain
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


def execute_ai_coach_brain(
    request: dict,
    ai_response: dict,
) -> dict:
    """
    Execute complete AI Coach brain.

    Flow:

    Request
       ↓
    Adapter
       ↓
    Gateway
       ↓
    Production Coach
    """

    return run_adapted_conversation(
        athlete_id=request["athlete_id"],
        question=request["question"],
        ai_response=ai_response,
        athlete_profile=request["athlete_profile"],
        training_history=request["training_history"],
        recovery_history=request["recovery_history"],
        decision_analysis=request["decision_analysis"],
        current_state=request["current_state"],
    )


def format_final_conversation_response(
    result: dict,
) -> dict:
    """
    Format final API conversation response.
    """

    return {
        "answer": result.get(
            "response",
            {},
        )
        .get(
            "personalised_response",
            {},
        )
        .get(
            "answer",
            "",
        ),
        "strategy": result.get(
            "response",
            {},
        ).get(
            "strategy",
            "",
        ),
        "confidence": result.get(
            "response",
            {},
        ).get(
            "confidence",
            50,
        ),
        "raw_response": result,
    }


def run_production_conversation_bridge(
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
    Main production conversation bridge.

    Final path:

    User Question
          ↓
    AI Coach Brain
          ↓
    Personalised Answer
    """

    request = build_production_conversation_request(
        athlete_id=athlete_id,
        question=question,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    result = execute_ai_coach_brain(
        request=request,
        ai_response=ai_response,
    )

    return format_final_conversation_response(
        result,
    )
