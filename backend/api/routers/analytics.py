from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.training_analytics_service import get_training_summary
from database.session import get_db

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get("/{athlete_id}/summary")
def training_summary(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    return get_training_summary(
        db,
        athlete_id,
    )
