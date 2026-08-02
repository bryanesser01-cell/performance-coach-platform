from api.services.ai_coach_conversation_migration_service import (
    migrate_conversation_response,
    prepare_migration_context,
    run_migrated_conversation,
)


def test_prepare_migration_context():

    result = prepare_migration_context(
        athlete_id=1,
        question="Should I train today?",
        athlete_profile={
            "sport": "running",
        },
        training_history=[],
        recovery_history=[],
        decision_analysis={},
        current_state={},
    )

    assert result["athlete_id"] == 1

    assert result["question"] == "Should I train today?"


def test_migrate_conversation_response():

    result = migrate_conversation_response(
        migration_context={
            "athlete_id": 1,
            "question": "Train?",
            "athlete_profile": {},
            "training_history": [],
            "recovery_history": [],
            "decision_analysis": {
                "REDUCE_TRAINING": {
                    "success_rate": 90,
                },
            },
            "current_state": {
                "readiness_score": 60,
            },
        },
        ai_response={
            "coach_message": ("Recover today."),
        },
    )

    assert result["strategy"] == "RECOVERY_FIRST"

    assert result["confidence"] == 90


def test_run_migrated_conversation():

    result = run_migrated_conversation(
        athlete_id=1,
        question="Should I reduce training?",
        ai_response={
            "coach_message": ("Reduce load."),
        },
        athlete_profile={},
        training_history=[],
        recovery_history=[],
        decision_analysis={
            "REDUCE_TRAINING": {
                "success_rate": 85,
            },
        },
        current_state={
            "readiness_score": 50,
        },
    )

    assert result["confidence"] == 85


def test_full_migration_pipeline():

    result = run_migrated_conversation(
        athlete_id=1,
        question="Should I do intervals?",
        ai_response={
            "coach_message": ("Adjust session."),
        },
        athlete_profile={
            "sport": "running",
        },
        training_history=[],
        recovery_history=[],
        decision_analysis={
            "REDUCE_TRAINING": {
                "success_rate": 95,
            },
        },
        current_state={
            "readiness_score": 70,
        },
    )

    assert result["strategy"] == "RECOVERY_FIRST"

    assert result["confidence"] == 95
