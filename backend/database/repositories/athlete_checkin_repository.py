from sqlalchemy.orm import Session

from database.models import AthleteCheckin


class AthleteCheckinRepository:
    """
    Repository for athlete daily check-in data.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        athlete_id: int,
        sleep_score: int,
        soreness_score: int,
        energy_score: int,
        motivation_score: int,
    ) -> AthleteCheckin:
        """
        Create athlete check-in.
        """

        checkin = AthleteCheckin(
            athlete_id=athlete_id,
            sleep_score=sleep_score,
            soreness_score=soreness_score,
            energy_score=energy_score,
            motivation_score=motivation_score,
        )

        self.db.add(
            checkin,
        )

        self.db.commit()

        self.db.refresh(
            checkin,
        )

        return checkin

    def get_latest_by_athlete_id(
        self,
        athlete_id: int,
    ) -> AthleteCheckin | None:
        """
        Retrieve latest athlete check-in.
        """

        return (
            self.db.query(
                AthleteCheckin,
            )
            .filter(
                AthleteCheckin.athlete_id
                == athlete_id,
            )
            .order_by(
                AthleteCheckin.created_at.desc(),
            )
            .first()
        )
