from sqlalchemy.orm import Session

from database.repositories.workout_block_repository import (
    WorkoutBlockRepository,
)


def analyse_workout_structure(
    db: Session,
    training_session_id: int,
) -> dict:
    """
    Analyse workout structure.

    Converts stored workout blocks
    into AI Coach readable format.
    """

    repository = WorkoutBlockRepository(
        db,
    )

    blocks = repository.get_blocks(
        training_session_id,
    )

    workout_blocks = []

    for block in blocks:

        details = []

        for detail in getattr(
            block,
            "details",
            [],
        ):

            details.append(
                {
                    "type": detail.detail_type,
                    "distance_meters": (detail.distance_meters),
                    "duration_minutes": (detail.duration_minutes),
                    "repetitions": (detail.repetitions),
                    "target": detail.target,
                    "recovery": detail.recovery,
                }
            )

        workout_blocks.append(
            {
                "block_type": (block.block_type),
                "description": (block.description),
                "details": details,
            }
        )

    return {
        "training_session_id": (training_session_id),
        "blocks": workout_blocks,
        "block_count": len(
            workout_blocks,
        ),
    }


def generate_workout_summary(
    workout_analysis: dict,
) -> str:
    """
    Create coach-friendly summary.
    """

    count = workout_analysis.get(
        "block_count",
        0,
    )

    return f"Workout contains {count} " "structured block(s)."
