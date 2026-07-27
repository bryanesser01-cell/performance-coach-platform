from api.services.performance_engine import analyse_training
from schemas.training import TrainingSessionResponse


def test_analyse_training():
    sessions = [
        TrainingSessionResponse(
            id=1,
            athlete_id=1,
            date="2026-07-27",
            session_type="easy",
            distance=5.0,
            duration=30.0,
            average_pace=6.0,
            average_hr=140,
            max_hr=160,
            cadence=170,
            elevation_gain=50,
            training_load=50,
            rpe=5,
            notes="Easy run",
        ),
        TrainingSessionResponse(
            id=2,
            athlete_id=1,
            date="2026-07-28",
            session_type="tempo",
            distance=8.0,
            duration=40.0,
            average_pace=5.0,
            average_hr=150,
            max_hr=170,
            cadence=175,
            elevation_gain=70,
            training_load=80,
            rpe=6,
            notes="Tempo run",
        ),
    ]

    result = analyse_training(
        sessions,
    )

    assert result is not None
    assert result.total_sessions == 2
    assert result.total_distance == 13.0
    assert result.total_training_load == 130.0
    assert result.longest_run == 8.0
