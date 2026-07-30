def store_research_reference(
    source_name: str,
    source_type: str,
    topic: str,
    evidence_level: str,
) -> dict:
    """
    Store evidence source reference.

    Examples:
    - AIS
    - Athletics Australia
    - World Athletics
    - Peer reviewed research
    """

    return {
        "source_name": source_name,
        "source_type": source_type,
        "topic": topic,
        "evidence_level": evidence_level,
    }



def classify_age_group(
    age: int,
) -> dict:
    """
    Classify athlete development stage.
    """

    if age < 12:

        category = "YOUTH_U12"

    elif age < 14:

        category = "YOUTH_U14"

    elif age < 18:

        category = "YOUTH_U18"

    elif age < 35:

        category = "ADULT"

    elif age < 50:

        category = "MASTERS"

    else:

        category = "MASTERS_PLUS"

    return {
        "age": age,
        "age_group": category,
    }



def apply_age_training_rules(
    age_group: str,
) -> dict:
    """
    Apply age-specific evidence rules.
    """

    rules = {

        "YOUTH_U12": [
            "movement_quality",
            "coordination",
            "skill_development",
            "safe_strength_foundation",
        ],

        "YOUTH_U14": [
            "technique",
            "athletic_development",
            "strength_foundation",
        ],

        "U18": [
            "progressive_strength",
            "power_development",
            "injury_prevention",
        ],

        "ADULT": [
            "performance_optimisation",
            "progressive_overload",
            "recovery_management",
        ],

        "MASTERS": [
            "strength_maintenance",
            "injury_prevention",
            "recovery_priority",
        ],

        "MASTERS_PLUS": [
            "mobility",
            "strength_retention",
            "recovery_focus",
        ],
    }


    return {
        "age_group": age_group,
        "training_rules": rules.get(
            age_group,
            [],
        ),
    }



def apply_event_specific_rules(
    event: str,
) -> dict:
    """
    Apply athletics event evidence rules.

    Event determines athletic demands.
    """

    event_rules = {

        "100m": [
            "acceleration",
            "maximum_speed",
            "explosive_power",
        ],

        "200m": [
            "speed",
            "power",
            "speed_endurance",
        ],

        "400m": [
            "speed_endurance",
            "lactate_tolerance",
            "power",
        ],

        "800m": [
            "speed",
            "aerobic_power",
            "race_pace",
        ],

        "1500m": [
            "running_economy",
            "aerobic_power",
            "power",
            "strength_power",
        ],

        "mile": [
            "running_economy",
            "speed_reserve",
            "aerobic_capacity",
        ],

        "3000m": [
            "aerobic_capacity",
            "strength_endurance",
            "fatigue_resistance",
        ],

        "5000m": [
            "aerobic_capacity",
            "running_economy",
            "durability",
        ],

        "10000m": [
            "aerobic_capacity",
            "fatigue_resistance",
            "endurance",
        ],

        "5K": [
            "aerobic_capacity",
            "running_economy",
        ],

        "10K": [
            "threshold",
            "endurance",
        ],

        "half_marathon": [
            "aerobic_endurance",
            "fuel_management",
            "durability",
        ],

        "marathon": [
            "endurance_development",
            "fuel_strategy",
            "fatigue_resistance",
        ],

        "trail": [
            "terrain_adaptation",
            "single_leg_strength",
            "elevation_strength",
        ],

        "ultra_marathon": [
            "resilience",
            "fatigue_resistance",
            "nutrition_strategy",
        ],
    }


    return {
        "event": event,
        "event_focus": event_rules.get(
            event,
            [
                "general_fitness",
            ],
        ),
    }



def apply_evidence_rules(
    age: int,
    event: str,
    goal: str,
) -> dict:
    """
    Combine:

    Age evidence
    Event evidence
    Goal

    into one evidence profile.
    """

    age_profile = classify_age_group(
        age=age,
    )


    age_rules = apply_age_training_rules(
        age_group=age_profile[
            "age_group"
        ],
    )


    event_rules = apply_event_specific_rules(
        event=event,
    )


    return {
        "athlete_age": age,
        "age_group": age_profile[
            "age_group"
        ],
        "event": event,
        "goal": goal,

        "age_rules": age_rules[
            "training_rules"
        ],

        "event_rules": event_rules[
            "event_focus"
        ],

        "evidence_applied": True,
    }



def generate_evidence_based_recommendation(
    age: int,
    event: str,
    goal: str,
) -> dict:
    """
    Generate evidence-based recommendation.

    Uses:

    - Athlete age
    - Event demands
    - Evidence sources
    """

    evidence = apply_evidence_rules(
        age=age,
        event=event,
        goal=goal,
    )


    return {
        "recommendation": (
            "Generate training using "
            "age and event specific evidence."
        ),

        "confidence": 90,

        "evidence": evidence,

        "sources": [
            "AIS",
            "Athletics Australia",
            "World Athletics",
            "Sports Science Research",
        ],
    }
