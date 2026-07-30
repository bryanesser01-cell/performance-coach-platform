from api.services.ai_coach_conversation_migration_service import (
    run_migrated_conversation,
)


def build_final_conversation_context(
    athlete_id: int,
    question: str,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Build final production conversation context.

    This is the final controller layer before
    the AI Coach brain executes.
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


def execute_final_ai_coach_path(
    context: dict,
    ai_response: dict,
) -> dict:
    """
    Execute final AI Coach production path.

    Flow:

    Conversation Service
            ↓
    Final Service
            ↓
    Migration Layer
            ↓
    Complete AI Coach Brain
            ↓
    Personalised Answer
    """

    return run_migrated_conversation(
        athlete_id=context[
            "athlete_id"
        ],
        question=context[
            "question"
        ],
        ai_response=ai_response,
        athlete_profile=context[
            "athlete_profile"
        ],
        training_history=context[
            "training_history"
        ],
        recovery_history=context[
            "recovery_history"
        ],
        decision_analysis=context[
            "decision_analysis"
        ],
        current_state=context[
            "current_state"
        ],
    )


def generate_final_conversation_output(
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
    Generate final production conversation output.

    This becomes the final response layer.
    """

    context = build_final_conversation_context(
        athlete_id=athlete_id,
        question=question,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return execute_final_ai_coach_path(
        context=context,
        ai_response=ai_response,
    )


def run_final_conversation_service(
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
    Final AI Coach conversation entry point.

    Production flow:

    User Question
          ↓
    AI Coach Brain
          ↓
    Personalised Response
    """

    return generate_final_conversation_output(
        athlete_id=athlete_id,
        question=question,
        ai_response=ai_response,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )
