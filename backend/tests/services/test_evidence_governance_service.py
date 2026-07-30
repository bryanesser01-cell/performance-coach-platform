from api.services.evidence_governance_service import (
    build_evidence_statement,
    classify_evidence_source,
    generate_training_disclaimer,
    validate_claim,
)


def test_classify_peer_reviewed_source():

    result = classify_evidence_source(
        "Journal of Strength and Conditioning Research"
    )

    assert (
        result["evidence_level"]
        == "PEER_REVIEWED_RESEARCH"
    )



def test_classify_ais_source():

    result = classify_evidence_source(
        "Australian Institute of Sport"
    )

    assert (
        result["endorsed"]
        is False
    )



def test_safe_evidence_statement():

    result = build_evidence_statement(
        [
            "Australian Institute of Sport",
            "Athletics Australia",
        ]
    )

    assert (
        result["endorsement_claim"]
        is False
    )



def test_block_unsafe_claim():

    result = validate_claim(
        "This program is approved by AIS"
    )

    assert (
        result["approved"]
        is False
    )



def test_disclaimer_exists():

    result = generate_training_disclaimer()

    assert (
        "science-informed"
        in result["disclaimer"]
    )
