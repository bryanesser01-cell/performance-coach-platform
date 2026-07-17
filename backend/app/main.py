from fastapi import FastAPI

from api.routers.health import router as health_router

app = FastAPI(
    title="Performance Coach API",
    version="0.1.0",
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Performance Coach API is running!"
    }