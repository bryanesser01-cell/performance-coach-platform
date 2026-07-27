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

    def create_from_data(
        self,
        athlete_data,
    ) -> Athlete:
        """
        Create athlete from input data.
        """

        athlete = Athlete(
            name=athlete_data.name,
            age=athlete_data.age,
            height_cm=athlete_data.height_cm,
            weight_kg=athlete_data.weight_kg,
            resting_hr=athlete_data.resting_hr,
            max_hr=athlete_data.max_hr,
            sport=athlete_data.sport,
            primary_event=athlete_data.primary_event,
            experience_level=athlete_data.experience_level,
            weekly_distance=athlete_data.weekly_distance,
            training_days_per_week=athlete_data.training_days_per_week,
            current_5k_time=athlete_data.current_5k_time,
            injury_status=athlete_data.injury_status,
        )

        self.db.add(athlete)
        self.db.commit()
        self.db.refresh(athlete)

        return athlete

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
