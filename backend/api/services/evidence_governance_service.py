from typing import List


def classify_evidence_source(
    source_name: str,
) -> dict:
    """
    Classify evidence source reliability.

    This identifies source type.
    It does NOT imply endorsement.
    """

    peer_reviewed_sources = [
        "Journal of Strength and Conditioning Research",
        "Medicine & Science in Sports & Exercise",
        "British Journal of Sports Medicine",
    ]

    consensus_sources = [
        "IOC Consensus Statements",
        "ACSM Position Stands",
    ]

    sporting_organisation_sources = [
        "Australian Institute of Sport",
        "Athletics Australia",
        "World Athletics",
    ]


    if source_name in peer_reviewed_sources:

        evidence_level = "PEER_REVIEWED_RESEARCH"

    elif source_name in consensus_sources:

        evidence_level = "EXPERT_CONSENSUS"

    elif source_name in sporting_organisation_sources:

        evidence_level = "SPORTING_ORGANISATION_GUIDANCE"

    else:

        evidence_level = "GENERAL_REFERENCE"


    return {
        "source": source_name,
        "evidence_level": evidence_level,

        # Important:
        # We never claim endorsement
        "endorsed": False,
    }



def build_evidence_statement(
    sources: List[str],
) -> dict:
    """
    Build safe evidence wording.
    """

    classified_sources = []

    for source in sources:

        classified_sources.append(
            classify_evidence_source(
                source
            )
        )


    return {
        "statement": (
            "Training recommendations are "
            "science-informed using athlete data, "
            "peer-reviewed research, consensus "
            "statements and publicly available "
            "guidance from recognised organisations."
        ),

        "sources": classified_sources,

        "endorsement_claim": False,
    }



def validate_claim(
    claim: str,
) -> dict:
    """
    Check for unsafe claims.
    """

    restricted_terms = [
        "approved by",
        "endorsed by",
        "guaranteed",
        "will prevent injury",
        "will improve performance",
    ]


    violations = []

    lower_claim = claim.lower()


    for term in restricted_terms:

        if term in lower_claim:

            violations.append(term)


    if violations:

        return {
            "approved": False,
            "violations": violations,
            "replacement": (
                "Recommendation informed by "
                "science-based training principles "
                "and athlete-specific data."
            ),
        }


    return {
        "approved": True,
        "violations": [],
        "replacement": claim,
    }



def generate_training_disclaimer() -> dict:
    """
    User-facing disclaimer.
    """

    return {
        "disclaimer": (
            "Training recommendations are "
            "science-informed and personalised "
            "using athlete information and "
            "established training principles. "
            "They are not medical advice and "
            "do not replace qualified coaching, "
            "medical, or allied health guidance."
        )
    }



def build_evidence_metadata(
    topic: str,
    sources: List[str],
) -> dict:
    """
    Attach evidence information
    to AI Coach recommendations.
    """

    return {
        "topic": topic,

        "methodology": (
            "Science-informed methodology"
        ),

        "evidence": build_evidence_statement(
            sources
        ),

        "disclaimer": (
            generate_training_disclaimer()
        ),
    }
