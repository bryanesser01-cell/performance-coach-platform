from api.services.ai_coach_learning_loop_service import (
    generate_learning_signal,
    record_coach_interaction,
    run_learning_loop,
    update_learning_memory,
)


def test_record_coach_interaction():

    result = record_coach_interaction(
        athlete_id=1,
        question="Should I train today?",
        decision="REDUCE_TRAINING",
        confidence=90,
        outcome="positive",
    )

    assert (
        result["athlete_id"]
        == 1
    )

    assert (
        result["decision"]
        == "REDUCE_TRAINING"
    )


def test_generate_learning_signal_positive():

    result = generate_learning_signal(
        decision="REDUCE_TRAINING",
        outcome="positive",
        confidence=90,
    )

    assert (
        result["signal"]
        == "REINFORCE"
    )


def test_generate_learning_signal_negative():

    result = generate_learning_signal(
        decision="PROGRESS_TRAINING",
        outcome="negative",
        confidence=80,
    )

    assert (
        result["signal"]
        == "ADJUST"
    )


def test_update_learning_memory():

    result = update_learning_memory(
        athlete_id=1,
        learning_signal={
            "signal": "REINFORCE",
        },
    )

    assert (
        result["learning_updated"]
        is True
    )


def test_run_learning_loop():

    result = run_learning_loop(
        athlete_id=1,
        question="Should I reduce training?",
        decision="REDUCE_TRAINING",
        confidence=90,
        outcome="positive",
    )

    assert (
        result["memory"]["learning_updated"]
        is True
    )

    assert (
        result["learning_signal"]["signal"]
        == "REINFORCE"
    )
