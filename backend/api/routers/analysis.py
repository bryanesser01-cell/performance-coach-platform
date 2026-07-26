from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.analysis_service import (
    analyse_athlete_service,
)
from database.database import get_db
from schemas.analysis import PerformanceAnalysis

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"],
)


@router.get(
    "/{athlete_id}",
    response_model=PerformanceAnalysis,
)
def analyse_athlete(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    return analyse_athlete_service(
        db,
        athlete_id,
    )
