import logging

from sqlalchemy.orm import Session

from core.exceptions import AthleteNotFoundError
from database.models import Athlete
from schemas.athlete import AthleteCreate

logger = logging.getLogger(__name__)


def create_athlete(
    db: Session,
    athlete_data: AthleteCreate,
) -> Athlete:
    """
    Create and persist a new athlete.
    """

    logger.info(
        "Saving athlete '%s' to the database.",
        athlete_data.name,
    )

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

    db.add(athlete)
    db.commit()
    db.refresh(athlete)

    logger.info(
        "Athlete '%s' saved with ID %s.",
        athlete.name,
        athlete.id,
    )

    return athlete


def get_all_athletes(
    db: Session,
) -> list[Athlete]:
    logger.info("Retrieving all athletes.")

    athletes = db.query(Athlete).all()

    logger.info(
        "Retrieved %s athletes.",
        len(athletes),
    )

    return athletes


def get_athlete_by_id(
    db: Session,
    athlete_id: int,
) -> Athlete:
    logger.info(
        "Looking up athlete ID %s.",
        athlete_id,
    )

    athlete = (
        db.query(Athlete)
        .filter(Athlete.id == athlete_id)
        .first()
    )

    if athlete is None:
        raise AthleteNotFoundError(
            f"Athlete {athlete_id} not found."
        )

    return athlete