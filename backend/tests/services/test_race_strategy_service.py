from api.services.race_strategy_service import (
    generate_race_strategy,
    get_race_checkpoints,
)


def test_1500m_checkpoints():

    checkpoints = get_race_checkpoints(
        "1500m",
    )

    assert checkpoints == [
        300,
        700,
        1100,
        1500,
    ]


def test_generate_1500m_race_strategy():

    strategy = generate_race_strategy(
        event="1500m",
        target_time="4:45",
    )

    assert (
        strategy["target_time"]
        == "4:45"
    )

    assert (
        strategy["checkpoints"][-1]
        ["distance"]
        == 1500
    )

    assert (
        strategy["checkpoints"][-1]
        ["cumulative_time"]
        == "4:45"
    )


def test_800m_strategy():

    strategy = generate_race_strategy(
        event="800m",
        target_time="2:20",
    )

    assert (
        strategy["checkpoints"][0]
        ["distance"]
        == 400
    )

    assert (
        strategy["checkpoints"][-1]
        ["distance"]
        == 800
    )
