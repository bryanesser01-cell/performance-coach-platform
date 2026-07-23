from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    app_name: str = "Performance Coach API"
    app_version: str = "0.1.0"

    environment: str = "development"
    log_level: str = "INFO"

    # Database
    database_url: str = "sqlite:///performance_coach.db"

    # Security
    secret_key: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    # Training thresholds
    min_weekly_sessions: int = 3
    min_weekly_distance: float = 20.0
    target_rpe: float = 7.0
    max_weekly_distance_increase: float = 0.10

    # Default workout settings
    default_easy_run_km: float = 8
    default_easy_run_minutes: int = 45

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()