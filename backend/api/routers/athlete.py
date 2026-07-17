from fastapi import APIRouter

from schemas.athlete import AthleteCreate
from api.services.performance import analyse_athlete
from api.services.athlete_profile import build_athlete_profile

router = APIRouter()


@router.post("/athletes")
def create_athlete(athlete: AthleteCreate):

    analysis = analyse_athlete(athlete)
    profile = build_athlete_profile(athlete)

    return {
        "message": "Athlete created successfully!",
        "athlete": athlete,
        "analysis": analysis,
        "profile": profile
    }