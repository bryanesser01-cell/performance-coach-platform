from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from database.athlete_models import Athlete
from database.user_models import User
from repositories.athlete_repository import AthleteRepository
from schemas.athlete_schema import AthleteCreate, AthleteUpdate


class AthleteService:
    def __init__(self, db: Session):
        self.repository = AthleteRepository(db)

    def create(
        self,
        current_user: User,
        athlete: AthleteCreate,
    ) -> Athlete:
        return self.repository.create(current_user.id, athlete)

    def get_all(self, current_user: User):
        return self.repository.get_by_user(current_user.id)

    def get(
        self,
        current_user: User,
        athlete_id: int,
    ) -> Athlete:
        athlete = self.repository.get_by_id(athlete_id)

        if athlete is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Athlete not found",
            )

        if athlete.user_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized",
            )

        return athlete

    def update(
        self,
        current_user: User,
        athlete_id: int,
        updates: AthleteUpdate,
    ) -> Athlete:
        athlete = self.get(current_user, athlete_id)
        return self.repository.update(athlete, updates)

    def delete(
        self,
        current_user: User,
        athlete_id: int,
    ) -> None:
        athlete = self.get(current_user, athlete_id)
        self.repository.delete(athlete)