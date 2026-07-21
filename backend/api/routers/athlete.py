from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db

from schemas.athlete import AthleteCreate

from api.services.athlete_service import (
    create_athlete,
    list_athletes,
)

router = APIRouter()


@router.get("/athletes")
def get_athletes(
    db: Session = Depends(get_db),
):
    return list_athletes(db)


@router.post("/athletes")
def add_athlete(
    athlete: AthleteCreate,
    db: Session = Depends(get_db),
):
    return create_athlete(
        db,
        athlete,
    )