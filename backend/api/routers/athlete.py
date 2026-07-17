from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.athlete import AthleteCreate
from api.services.performance import analyse_athlete
from api.services.athlete_profile import build_athlete_profile
from api.services.database_service import create_athlete as create_athlete_record
from api.services.database_service import get_all_athletes

from database.database import get_db


router = APIRouter()

@router.get("/athletes")
def list_athletes(
    db: Session = Depends(get_db)
):
    athletes = get_all_athletes(db)
    return athletes


@router.post("/athletes")
def create_athlete(
    athlete: AthleteCreate,
    db: Session = Depends(get_db)
):

    analysis = analyse_athlete(athlete)
    profile = build_athlete_profile(athlete)
    saved_athlete = create_athlete_record(db, athlete)

    return {
        "message": "Athlete created successfully!",
        "athlete": {
            "id": saved_athlete.id,
            "name": saved_athlete.name,
            "age": saved_athlete.age,
        },
        "analysis": analysis,
        "profile": profile,
    }