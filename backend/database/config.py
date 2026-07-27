from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class DatabaseSettings:
    host: str = getenv("DB_HOST", "localhost")
    port: int = int(getenv("DB_PORT", "5433"))
    database: str = getenv("DB_NAME", "performance_coach")
    username: str = getenv("DB_USER", "performance")
    password: str = getenv("DB_PASSWORD", "performance")

    @property
    def url(self) -> str:
        return (
            f"postgresql+psycopg://"
            f"{self.username}:{self.password}"
            f"@{self.host}:{self.port}"
            f"/{self.database}"
        )


settings = DatabaseSettings()
