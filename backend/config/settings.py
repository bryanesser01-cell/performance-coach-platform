from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------

    app_name: str = "Performance Coach API"
    app_version: str = "0.1.0"

    environment: str = "development"
    log_level: str = "INFO"

    # ------------------------------------------------------------------
    # Database
    # ------------------------------------------------------------------

    database_url: str = "sqlite:///performance_coach.db"

    # ------------------------------------------------------------------
    # Security
    # ------------------------------------------------------------------

    secret_key: str = Field(
        ...,
        description="JWT signing secret key.",
    )

    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    # ------------------------------------------------------------------
    # Performance Analysis
    # ------------------------------------------------------------------

    analysis_window_days: int = 7

    # ------------------------------------------------------------------
    # Training Thresholds
    # ------------------------------------------------------------------

    min_weekly_sessions: int = 3
    min_weekly_distance: float = 20.0
    target_rpe: float = 7.0

    # Maximum safe weekly increase (10%)
    max_weekly_distance_increase: float = 0.10

    # Maximum recommended weekly training load
    max_recommended_training_load: float = 500.0

    # ------------------------------------------------------------------
    # Goal Analysis
    # ------------------------------------------------------------------

    recent_training_sessions: int = 10
    minimum_goal_confidence: float = 0.60

    # ------------------------------------------------------------------
    # Default Workout Settings
    # ------------------------------------------------------------------

    default_easy_run_km: float = 8.0
    default_easy_run_minutes: int = 45

    # ------------------------------------------------------------------
    # Pydantic Settings
    # ------------------------------------------------------------------

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
