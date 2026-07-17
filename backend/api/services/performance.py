from schemas.athlete import AthleteCreate


def analyse_athlete(athlete: AthleteCreate):

    bmi = round(
        athlete.weight_kg /
        ((athlete.height_cm / 100) ** 2),
        1
    )

    heart_rate_reserve = athlete.max_hr - athlete.resting_hr

    zone2_low = round(athlete.resting_hr + heart_rate_reserve * 0.60)
    zone2_high = round(athlete.resting_hr + heart_rate_reserve * 0.70)

    return {
        "bmi": bmi,
        "zone2": f"{zone2_low}-{zone2_high}",
        "sport": athlete.sport,
        "event": athlete.primary_event
    }