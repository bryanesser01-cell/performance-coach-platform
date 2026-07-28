from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.athlete_performance_report_service import (
    generate_athlete_performance_report,
)
from database.session import get_db

router = APIRouter(
    prefix="/athletes",
    tags=["Athlete Performance Report"],
)


@router.get("/{athlete_id}/performance-report")
def get_athlete_performance_report(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    """
    Generate complete athlete performance report.
    """

    return generate_athlete_performance_report(
        db,
        athlete_id,
    )
