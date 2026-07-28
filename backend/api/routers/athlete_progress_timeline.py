from fastapi import APIRouter

router = APIRouter(
    prefix="/athletes",
    tags=["Athlete Progress Timeline"],
)


@router.get("/{athlete_id}/progress-timeline")
def get_progress_timeline(
    athlete_id: int,
):
    """
    Return athlete progress timeline.
    """

    return {
        "athlete_id": athlete_id,
        "period": "12_weeks",
        "fitness_trend": "improving",
        "milestones": [
            "Training history analysed.",
        ],
    }
