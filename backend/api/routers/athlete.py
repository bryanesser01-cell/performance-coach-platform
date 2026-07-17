from fastapi import APIRouter

from schemas.athlete import AthleteCreate
from api.services.performance import analyse_athlete

router = APIRouter()


@router.post("/athletes")
def create_athlete(athlete: AthleteCreate):

    analysis = analyse_athlete(athlete)

    return {
        "message": "Athlete created successfully!",
        "athlete": athlete,
        "analysis": analysis
    }