from api.services.ai_coach_legacy_cleanup_service import (
    remove_legacy_controller_path,
    remove_legacy_formatter_path,
    verify_single_pipeline,
)


def test_remove_legacy_controller_path():

    result = remove_legacy_controller_path(
        athlete_id=1,
        question="Should I train today?",
        response={
            "decision": "REDUCE_TRAINING",
            "confidence": 90,
            "outcome": "positive",
        },
    )

    assert result["success"] is True

    assert result["data"]["learning_applied"] is True


def test_remove_legacy_formatter_path():

    result = remove_legacy_formatter_path(
        athlete_id=1,
        question="Should I recover?",
        response={
            "decision": "RECOVERY",
            "confidence": 85,
            "outcome": "positive",
        },
    )

    assert result["success"] is True

    assert result["data"]["learning_applied"] is True


def test_verify_single_pipeline():

    result = verify_single_pipeline(
        {
            "success": True,
            "data": {
                "learning_applied": True,
            },
        },
    )

    assert result["single_pipeline_active"] is True
