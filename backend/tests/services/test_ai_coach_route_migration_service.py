from api.services.ai_coach_route_migration_service import (
    migrate_chat_route,
    migrate_conversation_route,
    validate_route_migration,
)


def test_migrate_conversation_route():

    result = migrate_conversation_route(
        athlete_id=1,
        question="Should I train today?",
        response={
            "decision": "REDUCE_TRAINING",
            "confidence": 90,
            "outcome": "positive",
        },
    )

    assert (
        result["success"]
        is True
    )

    assert (
        result["data"]["learning_applied"]
        is True
    )


def test_migrate_chat_route():

    result = migrate_chat_route(
        athlete_id=1,
        question="Should I recover?",
        response={
            "decision": "RECOVERY",
            "confidence": 85,
            "outcome": "positive",
        },
    )

    assert (
        result["success"]
        is True
    )

    assert (
        result["data"]["learning_applied"]
        is True
    )


def test_validate_route_migration():

    result = validate_route_migration(
        {
            "success": True,
            "data": {
                "learning_applied": True,
            },
        },
    )

    assert (
        result["valid"]
        is True
    )
