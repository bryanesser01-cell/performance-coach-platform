from api.models.coach_context import CoachContext
from api.services.coach_pipeline import CoachPipeline


def test_pipeline_executes_steps():

    context = CoachContext(
        athlete_id=1,
    )

    pipeline = CoachPipeline()

    def step_one(ctx: CoachContext):
        ctx.metadata["one"] = True

    def step_two(ctx: CoachContext):
        ctx.metadata["two"] = True

    pipeline.add_step(step_one)
    pipeline.add_step(step_two)

    pipeline.run(context)

    assert context.metadata["one"] is True
    assert context.metadata["two"] is True


def test_pipeline_returns_context():

    context = CoachContext(
        athlete_id=1,
    )

    pipeline = CoachPipeline()

    result = pipeline.run(context)

    assert result is context
