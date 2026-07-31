from sqlalchemy.orm import Session

from database.repositories.athlete_memory_repository import (
    AthleteMemoryRepository,
)


def remember(
    db: Session,
    athlete_id: int,
    memory_type: str,
    memory_value: str,
):
    """
    Store important athlete context.

    Examples:
    - goal
    - preference
    - race
    - injury
    - performance_improvement
    - training_response
    """

    repository = AthleteMemoryRepository(
        db,
    )

    return repository.create(
        athlete_id=athlete_id,
        memory_type=memory_type,
        memory_value=memory_value,
    )


def remember_performance(
    db: Session,
    athlete_id: int,
    event: str,
    previous_value: str,
    current_value: str,
):
    """
    Store performance improvement memory.

    Example:
    5K improved from 23:05 to 22:30.
    """

    return remember(
        db,
        athlete_id,
        "performance_improvement",
        (
            f"{event}: improved from "
            f"{previous_value} to {current_value}"
        ),
    )


def remember_training_response(
    db: Session,
    athlete_id: int,
    training_block: str,
    response: str,
):
    """
    Store athlete response to training.
    """

    return remember(
        db,
        athlete_id,
        "training_response",
        (
            f"{training_block}: {response}"
        ),
    )


def remember_race_result(
    db: Session,
    athlete_id: int,
    race: str,
    result: str,
):
    """
    Store race history memory.
    """

    return remember(
        db,
        athlete_id,
        "race_result",
        (
            f"{race}: {result}"
        ),
    )


def recall(
    db: Session,
    athlete_id: int,
) -> list:
    """
    Retrieve all memories for athlete.
    """

    repository = AthleteMemoryRepository(
        db,
    )

    return repository.get_by_athlete_id(
        athlete_id,
    )


def recall_by_type(
    db: Session,
    athlete_id: int,
    memory_type: str,
) -> list:
    """
    Retrieve memories by category.
    """

    repository = AthleteMemoryRepository(
        db,
    )

    return repository.get_by_type(
        athlete_id=athlete_id,
        memory_type=memory_type,
    )


def build_memory_context(
    memories: list,
) -> dict:
    """
    Convert stored memories into AI coach context.
    """

    context = {}

    for memory in memories:
        context.setdefault(
            memory.memory_type,
            [],
        )

        context[memory.memory_type].append(
            memory.memory_value,
        )

    return context


def get_memory_summary(
    memories: list,
) -> dict:
    """
    Create high-level athlete memory summary.
    """

    context = build_memory_context(
        memories,
    )

    return {
        "memory_count": len(memories),
        "categories": list(
            context.keys(),
        ),
        "memory_context": context,
        "memory_ready": bool(memories),
    }
