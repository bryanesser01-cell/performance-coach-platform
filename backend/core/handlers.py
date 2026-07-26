from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from core.exceptions import (
    AthleteNotFoundError,
    GoalNotFoundError,
    InvalidTrainingDataError,
    TrainingSessionNotFoundError,
)


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(AthleteNotFoundError)
    async def athlete_not_found_handler(
        request: Request,
        exc: AthleteNotFoundError,
    ):
        return JSONResponse(
            status_code=404,
            content={"detail": str(exc)},
        )

    @app.exception_handler(GoalNotFoundError)
    async def goal_not_found_handler(
        request: Request,
        exc: GoalNotFoundError,
    ):
        return JSONResponse(
            status_code=404,
            content={"detail": str(exc)},
        )

    @app.exception_handler(TrainingSessionNotFoundError)
    async def training_not_found_handler(
        request: Request,
        exc: TrainingSessionNotFoundError,
    ):
        return JSONResponse(
            status_code=404,
            content={"detail": str(exc)},
        )

    @app.exception_handler(InvalidTrainingDataError)
    async def invalid_training_handler(
        request: Request,
        exc: InvalidTrainingDataError,
    ):
        return JSONResponse(
            status_code=400,
            content={"detail": str(exc)},
        )
