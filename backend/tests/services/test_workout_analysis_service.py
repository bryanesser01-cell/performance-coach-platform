from unittest.mock import Mock, patch

from api.services.workout_analysis_service import (
    analyse_workout_structure,
    generate_workout_summary,
)


def test_workout_analysis_returns_blocks():

    db = Mock()

    block = Mock()

    block.block_type = "main_set"

    block.description = "Speed endurance"

    detail = Mock()

    detail.detail_type = "interval"

    detail.distance_meters = 200

    detail.duration_minutes = None

    detail.repetitions = 4

    detail.target = "40 seconds"

    detail.recovery = "60 seconds"

    block.details = [
        detail,
    ]

    with patch(
        "api.services.workout_analysis_service.WorkoutBlockRepository",
    ) as repository:

        repository.return_value.get_blocks.return_value = [
            block,
        ]

        result = analyse_workout_structure(
            db=db,
            training_session_id=1,
        )

    assert result["block_count"] == 1

    assert result["blocks"][0]["details"][0]["distance_meters"] == 200


def test_generate_workout_summary():

    summary = generate_workout_summary(
        {
            "block_count": 3,
        }
    )

    assert summary == "Workout contains 3 structured block(s)."
