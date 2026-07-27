from api.services.performance_engine_service import (
    calculate_performance_score,
)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db

router = APIRouter(
    prefix="/performance",
    tags=["Performance"],
)


@router.get("/{athlete_id}")
def get_performance_score(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    return calculate_performance_score(
        db,
        athlete_id,
    )
