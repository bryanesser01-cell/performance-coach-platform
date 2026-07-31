from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.athlete_dashboard_intelligence_service import (
    generate_dashboard_intelligence,
)
from api.services.athlete_dashboard_service import (
    generate_fitness_summary,
    generate_prediction,
    generate_race_readiness,
    generate_training_status,
)
from api.services.dashboard_insight_service import (
    generate_dashboard_insight,
)
from api.services.performance_scorecard_service import (
    generate_performance_scorecard,
)
from api.services.performance_timeline_service import (
    analyse_timeline_progress,
    create_performance_timeline,
)
from database.session import get_db

router = APIRouter(
    prefix="/athletes",
    tags=["Athlete Dashboard"],
)


@router.get("/{athlete_id}/fitness-summary")
def get_fitness_summary(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    return generate_fitness_summary(
        db,
        athlete_id,
    )


@router.get("/{athlete_id}/training-status")
def get_training_status(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    return generate_training_status(
        db,
        athlete_id,
    )


@router.get("/{athlete_id}/race-readiness")
def get_race_readiness(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    return generate_race_readiness(
        db,
        athlete_id,
    )


@router.get("/{athlete_id}/prediction")
def get_prediction(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    return generate_prediction(
        db,
        athlete_id,
    )


@router.get("/{athlete_id}/dashboard")
def get_dashboard(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    """
    Complete athlete dashboard intelligence.
    """

    scorecard = generate_performance_scorecard(
        fitness_score=90,
        consistency_score=85,
        readiness_score=88,
        improvement_score=82,
        trend="improving",
    )

    timeline = create_performance_timeline(
        [
            {
                "event": "5K",
                "value": "23:05",
                "date": "2026-01-01",
                "improved": False,
            },
            {
                "event": "5K",
                "value": "22:30",
                "date": "2026-06-01",
                "improved": True,
            },
        ]
    )

    timeline_analysis = analyse_timeline_progress(
        timeline["milestones"],
    )

    insight = generate_dashboard_insight(
        scorecard,
        timeline_analysis,
        {
            "limiter": "speed",
        },
    )

    return {
        "athlete_id": athlete_id,
        "fitness_summary": generate_fitness_summary(
            db,
            athlete_id,
        ),
        "training_status": generate_training_status(
            db,
            athlete_id,
        ),
        "race_readiness": generate_race_readiness(
            db,
            athlete_id,
        ),
        "prediction": generate_prediction(
            db,
            athlete_id,
        ),
        "scorecard": scorecard,
        "timeline": timeline_analysis,
        "insight": insight,
    }


@router.get("/{athlete_id}/intelligence")
def get_dashboard_intelligence(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    """
    Generate athlete performance intelligence.
    """

    intelligence = generate_dashboard_intelligence(
        generate_fitness_summary(
            db,
            athlete_id,
        ),
        generate_training_status(
            db,
            athlete_id,
        ),
        generate_race_readiness(
            db,
            athlete_id,
        ),
        generate_prediction(
            db,
            athlete_id,
        ),
        {
            "trend": "improving",
        },
        {
            "limiter": "speed",
        },
    )

    return {
        "athlete_id": athlete_id,
        "intelligence": intelligence,
    }
