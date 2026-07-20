from sqlalchemy.orm import Session

from database.models import Athlete


def create_athlete(db: Session, athlete_data):
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

    return athlete


def get_all_athletes(db: Session):
    return db.query(Athlete).all()


def get_athlete_by_id(db: Session, athlete_id: int):
    return (
        db.query(Athlete)
        .filter(Athlete.id == athlete_id)
        .first()
    )