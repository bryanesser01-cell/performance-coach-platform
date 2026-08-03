from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RecoveryAssessment:
    """
    Result of analysing athlete recovery.
    """

    recovery_score: float

    status: str

    message: str

    recommendation: str
