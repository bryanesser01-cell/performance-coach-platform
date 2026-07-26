from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.recommendation_service import (
    get_recommendations_service,
)
from database.database import get_db
from schemas.recommendation_response import (
    RecommendationResponse,
)

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"],
)


@router.get(
    "/{athlete_id}",
    response_model=RecommendationResponse,
)
def get_recommendations(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    return get_recommendations_service(
        db,
        athlete_id,
    )
