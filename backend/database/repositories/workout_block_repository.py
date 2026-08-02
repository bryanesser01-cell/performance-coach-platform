from sqlalchemy.orm import Session

from database.workout_models import (
    WorkoutBlock,
    WorkoutDetail,
)


class WorkoutBlockRepository:
    """
    Repository for workout structure.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create_block(
        self,
        training_session_id: int,
        block_type: str,
        description: str | None = None,
        order_number: int = 1,
    ):

        block = WorkoutBlock(
            training_session_id=(training_session_id),
            block_type=block_type,
            description=description,
            order_number=order_number,
        )

        self.db.add(
            block,
        )

        self.db.commit()

        self.db.refresh(
            block,
        )

        return block

    def add_detail(
        self,
        workout_block_id: int,
        detail_type: str,
        distance_meters: int | None = None,
        duration_minutes: int | None = None,
        repetitions: int | None = None,
        target: str | None = None,
        recovery: str | None = None,
        notes: str | None = None,
    ):

        detail = WorkoutDetail(
            workout_block_id=(workout_block_id),
            detail_type=detail_type,
            distance_meters=distance_meters,
            duration_minutes=duration_minutes,
            repetitions=repetitions,
            target=target,
            recovery=recovery,
            notes=notes,
        )

        self.db.add(
            detail,
        )

        self.db.commit()

        self.db.refresh(
            detail,
        )

        return detail

    def get_blocks(
        self,
        training_session_id: int,
    ):

        blocks = (
            self.db.query(
                WorkoutBlock,
            )
            .filter(
                WorkoutBlock.training_session_id == training_session_id,
            )
            .order_by(
                WorkoutBlock.order_number,
            )
            .all()
        )

        if not isinstance(
            blocks,
            list,
        ):
            return []

        for block in blocks:

            block.details = self.get_details(
                block.id,
            )

        return blocks

    def get_details(
        self,
        workout_block_id: int,
    ):

        details = (
            self.db.query(
                WorkoutDetail,
            )
            .filter(
                WorkoutDetail.workout_block_id == workout_block_id,
            )
            .all()
        )

        if not isinstance(
            details,
            list,
        ):
            return []

        return details
