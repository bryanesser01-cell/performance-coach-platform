from api.services.ai_coach_conversation_cutover_service import (
    run_conversation_cutover,
)


def prepare_migration_context(
    athlete_id: int,
    question: str,
    athlete_profile: dict,
    training_history: list[dict],
    recovery_history: list[dict],
    decision_analysis: dict,
    current_state: dict,
) -> dict:
    """
    Prepare existing conversation service data
    for the new AI Coach production path.
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


def migrate_conversation_response(
    migration_context: dict,
    ai_response: dict,
) -> dict:
    """
    Move conversation response through
    the new AI Coach brain.
    """

    return run_conversation_cutover(
        athlete_id=migration_context["athlete_id"],
        question=migration_context["question"],
        ai_response=ai_response,
        athlete_profile=migration_context["athlete_profile"],
        training_history=migration_context["training_history"],
        recovery_history=migration_context["recovery_history"],
        decision_analysis=migration_context["decision_analysis"],
        current_state=migration_context["current_state"],
    )


def run_migrated_conversation(
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
    Main migration entry point.

    Old Conversation Service
            ↓
    Migration Layer
            ↓
    Full AI Coach Brain
            ↓
    Personalised Response
    """

    context = prepare_migration_context(
        athlete_id=athlete_id,
        question=question,
        athlete_profile=athlete_profile,
        training_history=training_history,
        recovery_history=recovery_history,
        decision_analysis=decision_analysis,
        current_state=current_state,
    )

    return migrate_conversation_response(
        migration_context=context,
        ai_response=ai_response,
    )
