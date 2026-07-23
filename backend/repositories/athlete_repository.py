from typing import List, Optional

from sqlalchemy.orm import Session

from database.athlete_models import Athlete
from schemas.athlete_schema import AthleteCreate, AthleteUpdate


class AthleteRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_id: int, athlete: AthleteCreate) -> Athlete:
        db_athlete = Athlete(
            user_id=user_id,
            **athlete.model_dump(),
        )

        self.db.add(db_athlete)
        self.db.commit()
        self.db.refresh(db_athlete)

        return db_athlete

    def get_by_id(self, athlete_id: int) -> Optional[Athlete]:
        return (
            self.db.query(Athlete)
            .filter(Athlete.id == athlete_id)
            .first()
        )

    def get_by_user(self, user_id: int) -> List[Athlete]:
        return (
            self.db.query(Athlete)
            .filter(Athlete.user_id == user_id)
            .all()
        )

    def update(
        self,
        athlete: Athlete,
        updates: AthleteUpdate,
    ) -> Athlete:
        for field, value in updates.model_dump(exclude_unset=True).items():
            setattr(athlete, field, value)

        self.db.commit()
        self.db.refresh(athlete)

        return athlete

    def delete(self, athlete: Athlete) -> None:
        self.db.delete(athlete)
        self.db.commit()