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
    """

    repository = AthleteMemoryRepository(
        db,
    )

    return repository.create(
        athlete_id=athlete_id,
        memory_type=memory_type,
        memory_value=memory_value,
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

    Examples:
    goal:
        "Break 20 minutes for 5K"

    preference:
        "Prefers morning training"
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
