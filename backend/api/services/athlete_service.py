import logging

from sqlalchemy.orm import Session

from api.services.performance import analyse_athlete
from api.services.athlete_profile import build_athlete_profile

from repositories.athlete_repository import AthleteRepository

from schemas.athlete import AthleteCreate

logger = logging.getLogger(__name__)


def create_athlete(
    db: Session,
    athlete: AthleteCreate,
):

    logger.info(
        "Creating athlete '%s'.",
        athlete.name,
    )

    analysis = analyse_athlete(athlete)

    profile = build_athlete_profile(athlete)

    repository = AthleteRepository(db)

    saved_athlete = repository.create(
        athlete
    )

    return {
        "message": "Athlete created successfully!",
        "athlete": {
            "id": saved_athlete.id,
            "name": saved_athlete.name,
            "age": saved_athlete.age,
            "height_cm": saved_athlete.height_cm,
            "weight_kg": saved_athlete.weight_kg,
            "resting_hr": saved_athlete.resting_hr,
            "max_hr": saved_athlete.max_hr,
            "sport": saved_athlete.sport,
            "primary_event": saved_athlete.primary_event,
            "experience_level": saved_athlete.experience_level,
            "weekly_distance": saved_athlete.weekly_distance,
            "training_days_per_week": saved_athlete.training_days_per_week,
            "current_5k_time": saved_athlete.current_5k_time,
            "injury_status": saved_athlete.injury_status,
        },
        "analysis": analysis,
        "profile": profile,
    }


def list_athletes(
    db: Session,
):
    repository = AthleteRepository(db)
    return repository.get_all()