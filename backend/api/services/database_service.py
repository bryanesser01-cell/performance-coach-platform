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
    )

    db.add(athlete)
    db.commit()
    db.refresh(athlete)

    return athlete