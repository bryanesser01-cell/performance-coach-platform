from database.repositories.training_load_repository import (
    TrainingLoadRepository,
)


def test_training_load_repository_exists():

    assert hasattr(
        TrainingLoadRepository,
        "calculate_training_load_status",
    )


def test_training_load_status_method():

    assert hasattr(
        TrainingLoadRepository,
        "get_recent_activity_count",
    )
