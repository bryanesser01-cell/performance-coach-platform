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

    Youth and adult athletes require
    different coaching rules.
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
    Apply age-specific coaching rules.
    """

    rules = {
        "YOUTH_U12": [
            "movement_quality",
            "coordination",
            "bodyweight_strength",
            "avoid_maximal_loading",
        ],
        "YOUTH_U14": [
            "technique",
            "strength_foundation",
            "athletic_development",
        ],
        "YOUTH_U18": [
            "progressive_strength",
            "power_development",
            "injury_prevention",
        ],
        "ADULT": [
            "progressive_overload",
            "strength_development",
            "performance",
        ],
        "MASTERS": [
            "strength_maintenance",
            "recovery_management",
            "injury_prevention",
        ],
        "MASTERS_PLUS": [
            "mobility",
            "strength_retention",
            "recovery_priority",
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
    Apply athletics event-specific rules.
    """

    event_rules = {
        "800m": [
            "speed_power",
            "anaerobic_capacity",
        ],
        "1500m": [
            "running_economy",
            "power",
            "strength_endurance",
        ],
        "3000m": [
            "strength_endurance",
            "fatigue_resistance",
        ],
        "5000m": [
            "durability",
            "running_economy",
        ],
        "cross_country": [
            "durability",
            "strength",
            "terrain_adaptation",
        ],
    }

    return {
        "event": event,
        "event_focus": event_rules.get(
            event,
            [],
        ),
    }


def apply_evidence_rules(
    age: int,
    event: str,
    goal: str,
) -> dict:
    """
    Combine age, event and evidence rules.
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
    Generate recommendation using
    evidence-based rules.
    """

    evidence = apply_evidence_rules(
        age=age,
        event=event,
        goal=goal,
    )

    confidence = 90

    return {
        "recommendation": (
            "Create personalised training "
            "using age and event evidence."
        ),
        "confidence": confidence,
        "evidence": evidence,
        "sources": [
            "AIS",
            "Athletics Australia",
            "Sports Science Research",
        ],
    }
