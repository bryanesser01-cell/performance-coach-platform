from collections import Counter


class MemoryReasoningService:
    """
    Converts raw memory context into coaching insights.
    """

    def analyse(
        self,
        memory_context: dict,
    ) -> dict:

        memories = memory_context.get("memories", [])
        decisions = memory_context.get("decisions", [])
        learning_events = memory_context.get(
            "learning_events",
            [],
        )

        reasoning = {
            "memory_count": len(memories),
            "decision_count": len(decisions),
            "learning_event_count": len(learning_events),
            "fatigue_trend": "unknown",
            "injury_risk": "unknown",
            "preferred_decision": None,
        }

        # Determine most common previous decision
        if decisions:
            decision_names = [
                getattr(d, "decision", None)
                for d in decisions
                if getattr(d, "decision", None)
            ]

            if decision_names:
                reasoning["preferred_decision"] = (
                    Counter(decision_names)
                    .most_common(1)[0][0]
                )

        # Estimate fatigue trend
        fatigue_memories = [
            m
            for m in memories
            if "fatigue"
            in str(getattr(m, "content", "")).lower()
        ]

        if len(fatigue_memories) >= 3:
            reasoning["fatigue_trend"] = "increasing"
        elif fatigue_memories:
            reasoning["fatigue_trend"] = "present"
        else:
            reasoning["fatigue_trend"] = "stable"

        # Estimate injury risk
        injury_memories = [
            m
            for m in memories
            if any(
                word in str(
                    getattr(m, "content", "")
                ).lower()
                for word in (
                    "injury",
                    "pain",
                    "sore",
                    "tight",
                )
            )
        ]

        if len(injury_memories) >= 3:
            reasoning["injury_risk"] = "high"
        elif injury_memories:
            reasoning["injury_risk"] = "moderate"
        else:
            reasoning["injury_risk"] = "low"

        return reasoning
