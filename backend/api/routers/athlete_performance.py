from fastapi import APIRouter

from api.services.athlete_performance_summary_service import (
    generate_performance_summary,
)

router = APIRouter(
    prefix="/athletes",
    tags=["Athlete Performance"],
)


@router.get("/{athlete_id}/performance-summary")
def get_performance_summary(
    athlete_id: int,
):
    """
    Generate athlete performance summary.
    """

    activities = [
        {
            "distance_km": 5,
            "duration_seconds": 1500,
            "training_load": 50,
        },
        {
            "distance_km": 10,
            "duration_seconds": 3000,
            "training_load": 100,
        },
    ]

    summary = generate_performance_summary(
        activities,
    )

    return {
        "athlete_id": athlete_id,
        **summary,
    }
