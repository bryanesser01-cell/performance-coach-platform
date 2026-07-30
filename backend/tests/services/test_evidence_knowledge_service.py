from api.services.evidence_knowledge_service import (
    apply_age_training_rules,
    apply_evidence_rules,
    classify_age_group,
    generate_evidence_based_recommendation,
    store_research_reference,
)


def test_store_research_reference():

    result = store_research_reference(
        source_name="AIS",
        source_type="organisation",
        topic="strength_training",
        evidence_level="high",
    )

    assert (
        result["source_name"]
        == "AIS"
    )


def test_classify_youth_age():

    result = classify_age_group(
        age=11,
    )

    assert (
        result["age_group"]
        == "YOUTH_U12"
    )


def test_classify_adult_age():

    result = classify_age_group(
        age=45,
    )

    assert (
        result["age_group"]
        == "MASTERS"
    )


def test_apply_age_training_rules():

    result = apply_age_training_rules(
        age_group="YOUTH_U12",
    )

    assert (
        "coordination"
        in result["training_rules"]
    )


def test_apply_evidence_rules():

    result = apply_evidence_rules(
        age=11,
        event="1500m",
        goal="improve performance",
    )

    assert (
        result["evidence_applied"]
        is True
    )

    assert (
        "power"
        in result["event_rules"]
    )


def test_generate_evidence_based_recommendation():

    result = generate_evidence_based_recommendation(
        age=11,
        event="1500m",
        goal="improve performance",
    )

    assert (
        result["confidence"]
        == 90
    )

    assert (
        "AIS"
        in result["sources"]
    )
