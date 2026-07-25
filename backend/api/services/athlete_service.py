from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from database.athlete_models import Athlete
from database.user_models import User
from repositories.athlete_repository import AthleteRepository
from schemas.athlete_schema import AthleteCreate, AthleteUpdate


class AthleteService:
    """
    Service responsible for Athlete business logic.
    """

    def __init__(self, db: Session):
        self.db = db
        self.repository = AthleteRepository(db)

    def create(
        self,
        current_user: User,
        athlete: AthleteCreate,
    ) -> Athlete:
        """
        Create an athlete for the current user.
        """
        return self.repository.create(current_user.id, athlete)

    def get_all(
        self,
        current_user: User,
    ) -> list[Athlete]:
        """
        Retrieve all athletes belonging to the current user.
        """
        return self.repository.get_by_user(current_user.id)

    def get(
        self,
        current_user: User,
        athlete_id: int,
    ) -> Athlete:
        """
        Retrieve a single athlete belonging to the current user.
        """
        athlete = self.repository.get_by_id_and_user(
            athlete_id,
            current_user.id,
        )

        if athlete is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Athlete not found",
            )

        return athlete

    def update(
        self,
        current_user: User,
        athlete_id: int,
        updates: AthleteUpdate,
    ) -> Athlete:
        """
        Update an athlete belonging to the current user.
        """
        athlete = self.get(current_user, athlete_id)
        return self.repository.update(athlete, updates)

    def delete(
        self,
        current_user: User,
        athlete_id: int,
    ) -> None:
        """
        Delete an athlete belonging to the current user.
        """
        athlete = self.get(current_user, athlete_id)
        self.repository.delete(athlete)
