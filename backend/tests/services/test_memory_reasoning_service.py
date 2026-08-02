from api.services.memory_reasoning_service import (
    MemoryReasoningService,
)


class FakeMemory:
    def __init__(self, content):
        self.content = content


class FakeDecision:
    def __init__(self, decision):
        self.decision = decision


def test_empty_memory_context():

    service = MemoryReasoningService()

    result = service.analyse({})

    assert result["memory_count"] == 0
    assert result["decision_count"] == 0
    assert result["learning_event_count"] == 0
    assert result["fatigue_trend"] == "stable"
    assert result["injury_risk"] == "low"
    assert result["preferred_decision"] is None


def test_detects_fatigue():

    service = MemoryReasoningService()

    context = {
        "memories": [
            FakeMemory("fatigue"),
            FakeMemory("high fatigue"),
            FakeMemory("fatigue after workout"),
        ]
    }

    result = service.analyse(context)

    assert result["fatigue_trend"] == "increasing"


def test_detects_injury():

    service = MemoryReasoningService()

    context = {
        "memories": [
            FakeMemory("calf pain"),
            FakeMemory("tight hamstring"),
        ]
    }

    result = service.analyse(context)

    assert result["injury_risk"] == "moderate"


def test_detects_preferred_decision():

    service = MemoryReasoningService()

    context = {
        "decisions": [
            FakeDecision("RECOVERY_SESSION"),
            FakeDecision("RECOVERY_SESSION"),
            FakeDecision("MAINTAIN_TRAINING"),
        ]
    }

    result = service.analyse(context)

    assert result["preferred_decision"] == "RECOVERY_SESSION"
