from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    app_name: str = "Performance Coach API"
    app_version: str = "0.1.0"
    environment: str = "development"
    log_level: str = "INFO"

    # Database
    database_url: str = "sqlite:///./performance_coach.db"

    # Authentication
    secret_key: str = "replace-me"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    # AI / Analysis
    analysis_window_days: int = 7
    max_recommended_training_load: float = 500.0
    recent_training_sessions: int = 10
    minimum_goal_confidence: float = 0.60

    # Training thresholds
    min_weekly_sessions: int = 3
    min_weekly_distance: float = 20.0
    target_rpe: float = 7.0
    max_weekly_distance_increase: float = 0.10

    # Default workouts
    default_easy_run_km: float = 8.0
    default_easy_run_minutes: int = 45

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()