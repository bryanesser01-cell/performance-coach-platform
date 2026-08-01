"""
Coach Pipeline

Executes AI Coach stages in sequence.
"""

from collections.abc import Callable

from api.models.coach_context import CoachContext


class CoachPipeline:
    """
    Executes the AI Coach pipeline.
    """

    def __init__(self) -> None:
        self._steps: list[Callable[[CoachContext], None]] = []

    def add_step(
        self,
        step: Callable[[CoachContext], None],
    ) -> None:
        """
        Register a pipeline step.
        """

        self._steps.append(step)

    def run(
        self,
        context: CoachContext,
    ) -> CoachContext:
        """
        Execute all pipeline steps.
        """

        for step in self._steps:
            step(context)

        return context
