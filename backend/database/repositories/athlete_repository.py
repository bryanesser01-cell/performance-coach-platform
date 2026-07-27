from sqlalchemy.orm import Session

from database.models import Athlete
from database.repositories.base_repository import BaseRepository


class AthleteRepository(BaseRepository[Athlete]):
    """
    Repository for athlete database operations.
    """

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(
            db,
            Athlete,
        )

    def get_by_name(
        self,
        name: str,
    ) -> Athlete | None:
        """
        Find athlete by name.
        """

        return (
            self.db.query(Athlete)
            .filter(
                Athlete.name == name,
            )
            .first()
        )

    def create(
        self,
        athlete: Athlete,
    ) -> Athlete:
        """
        Create a new athlete.
        """

        self.db.add(athlete)
        self.db.commit()
        self.db.refresh(athlete)

        return athlete
