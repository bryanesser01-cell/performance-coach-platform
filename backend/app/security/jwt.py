from datetime import datetime, timedelta, timezone
from typing import Any

from fastapi import HTTPException, status
from jose import JWTError, jwt

from config.settings import settings

INVALID_TOKEN_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid or expired token.",
    headers={"WWW-Authenticate": "Bearer"},
)


def create_access_token(data: dict[str, Any]) -> str:
    """
    Create a signed JWT access token.
    """

    now = datetime.now(timezone.utc)

    payload = data.copy()

    payload.update(
        {
            "exp": now + timedelta(minutes=settings.access_token_expire_minutes),
            "iat": now,
            "type": "access",
        }
    )

    return jwt.encode(
        payload,
        settings.secret_key,
        algorithm=settings.jwt_algorithm,
    )


def verify_token(token: str) -> dict[str, Any]:
    """
    Validate and decode a JWT access token.
    """

    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.jwt_algorithm],
        )

        if payload.get("type") != "access":
            raise INVALID_TOKEN_EXCEPTION

        return payload

    except JWTError:
        raise INVALID_TOKEN_EXCEPTION
