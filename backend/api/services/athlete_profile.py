from schemas.athlete import AthleteCreate


def build_athlete_profile(athlete: AthleteCreate):

    sport = athlete.sport.lower()
    event = athlete.primary_event.lower()

    if sport == "running":

        if event in ["100m", "200m", "400m"]:
            return {
                "athlete_type": "Sprinter",
                "training_focus": "Speed & Power",
                "energy_system": "ATP-PC",
                "training_split": "60% speed / 40% strength"
            }

        elif event in ["800m", "1500m"]:
            return {
                "athlete_type": "Middle Distance Runner",
                "training_focus": "Speed Endurance",
                "energy_system": "Aerobic + Anaerobic",
                "training_split": "70% aerobic / 30% quality"
            }

        elif event in ["3k", "5k", "10k", "half marathon", "marathon"]:
            return {
                "athlete_type": "Distance Runner",
                "training_focus": "Aerobic Endurance",
                "energy_system": "Aerobic",
                "training_split": "80% easy / 20% hard"
            }

    elif sport == "cycling":
        return {
            "athlete_type": "Cyclist",
            "training_focus": "Endurance & Power",
            "energy_system": "Aerobic"
        }

    elif sport == "swimming":
        return {
            "athlete_type": "Swimmer",
            "training_focus": "Technique & Conditioning",
            "energy_system": "Mixed"
        }

    return {
        "athlete_type": "General Athlete",
        "training_focus": "General Fitness"
    }