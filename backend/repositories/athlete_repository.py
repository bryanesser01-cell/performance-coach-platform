from sqlalchemy.orm import Session

from database.models import Athlete
from schemas.athlete import AthleteCreate, AthleteUpdate


class AthleteRepository:
    """
    Repository responsible for all athlete database operations.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Athlete]:
        """
        Retrieve all athletes.
        """
        return (
            self.db.query(Athlete)
            .order_by(Athlete.id)
            .all()
        )

    def get_by_id(self, athlete_id: int) -> Athlete | None:
        """
        Retrieve an athlete by ID.
        """
        return (
            self.db.query(Athlete)
            .filter(Athlete.id == athlete_id)
            .first()
        )

    def create(self, athlete: AthleteCreate) -> Athlete:
        """
        Create a new athlete.
        """

        db_athlete = Athlete(
            **athlete.model_dump()
        )

        self.db.add(db_athlete)
        self.db.commit()
        self.db.refresh(db_athlete)

        return db_athlete

    def update(
        self,
        athlete_id: int,
        athlete: AthleteUpdate,
    ) -> Athlete | None:
        """
        Update an existing athlete.
        """

        db_athlete = self.get_by_id(athlete_id)

        if db_athlete is None:
            return None

        update_data = athlete.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_athlete,
                key,
                value,
            )

        self.db.commit()
        self.db.refresh(db_athlete)

        return db_athlete

    def delete(
        self,
        athlete_id: int,
    ) -> bool:
        """
        Delete an athlete.
        """

        athlete = self.get_by_id(
            athlete_id
        )

        if athlete is None:
            return False

        self.db.delete(athlete)
        self.db.commit()

        return True