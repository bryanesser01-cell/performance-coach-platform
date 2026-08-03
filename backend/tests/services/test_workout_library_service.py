from api.services.workout_library_service import (
    WorkoutLibraryService,
)


def test_recovery_run():

    library = WorkoutLibraryService()

    workout = library.recovery_run()

    assert workout["session_type"] == "Recovery Run"
    assert workout["intensity"] == "very_easy"


def test_easy_run():

    library = WorkoutLibraryService()

    workout = library.easy_run()

    assert workout["session_type"] == "Easy Run"
    assert workout["duration_minutes"] == 45


def test_threshold_run():

    library = WorkoutLibraryService()

    workout = library.threshold_run()

    assert workout["session_type"] == "Threshold Run"
    assert "threshold" in workout["main_set"].lower()


def test_vo2_max():

    library = WorkoutLibraryService()

    workout = library.vo2_max()

    assert workout["session_type"] == "VO₂ Max Intervals"


def test_long_run():

    library = WorkoutLibraryService()

    workout = library.long_run()

    assert workout["duration_minutes"] == 90


def test_tempo_run():

    library = WorkoutLibraryService()

    workout = library.tempo_run()

    assert workout["session_type"] == "Tempo Run"


def test_taper_run():

    library = WorkoutLibraryService()

    workout = library.taper_run()

    assert workout["session_type"] == "Taper Session"
    assert workout["intensity"] == "easy"
