from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.athlete import AthleteCreate
from api.services.database_service import get_all_athletes
from api.services.athlete_service import (
    create_athlete as create_athlete_service,
)
from database.database import get_db

router = APIRouter()


@router.get("/athletes")
def list_athletes(
    db: Session = Depends(get_db),
):
    return get_all_athletes(db)


@router.post("/athletes")
def create_athlete(
    athlete: AthleteCreate,
    db: Session = Depends(get_db),
):
    return create_athlete_service(
        db,
        athlete,
    )