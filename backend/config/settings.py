from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Training thresholds
    MIN_WEEKLY_SESSIONS: int = 3
    MIN_WEEKLY_DISTANCE: float = 20.0
    TARGET_RPE: float = 7.0
    MAX_WEEKLY_DISTANCE_INCREASE: float = 0.10

    # Default workout settings
    DEFAULT_EASY_RUN_KM: float = 8
    DEFAULT_EASY_RUN_MINUTES: int = 45

    class Config:
        env_file = ".env"


settings = Settings()