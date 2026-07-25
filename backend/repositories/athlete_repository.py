from typing import Any

from sqlalchemy.orm import Session

from database.athlete_models import Athlete
from repositories.base_repository import BaseRepository


class AthleteRepository(BaseRepository[Athlete]):
    """
    Repository responsible for all Athlete database operations.
    """

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(Athlete, db)

    def get_by_id_and_user(
        self,
        athlete_id: int,
        user_id: int,
    ) -> Athlete | None:
        """
        Retrieve an athlete by ID that belongs to the specified user.
        """
        return (
            self.db.query(Athlete)
            .filter(
                Athlete.id == athlete_id,
                Athlete.user_id == user_id,
            )
            .first()
        )

    def get_by_user(
        self,
        user_id: int,
    ) -> list[Athlete]:
        """
        Retrieve all athletes belonging to a user.
        """
        return (
            self.db.query(Athlete)
            .filter(Athlete.user_id == user_id)
            .order_by(Athlete.created_at.desc())
            .all()
        )

    def update(
        self,
        athlete: Athlete,
        updates: dict[str, Any],
    ) -> Athlete:
        """
        Update an existing athlete.
        """
        return super().update(
            athlete,
            updates,
        )
