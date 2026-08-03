from api.models.assessments.recovery_assessment import (
    RecoveryAssessment,
)


def test_create_recovery_assessment():

    assessment = RecoveryAssessment(
        recovery_score=87.5,
        status="ready",
        message="Recovery is excellent.",
        recommendation="Proceed with quality training.",
    )

    assert assessment.recovery_score == 87.5

    assert assessment.status == "ready"

    assert assessment.recommendation == "Proceed with quality training."
