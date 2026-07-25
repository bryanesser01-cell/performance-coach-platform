from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.security.jwt import verify_token
from database.database import get_db
from database.user_models import User
from repositories.user_repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

UNAUTHORIZED_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid authentication credentials.",
    headers={"WWW-Authenticate": "Bearer"},
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    """
    Validate the JWT access token and return the
    authenticated user.
    """

    payload = verify_token(token)

    user_id = payload.get("sub")

    if user_id is None:
        raise UNAUTHORIZED_EXCEPTION

    repository = UserRepository(db)

    user = repository.get_by_id(int(user_id))

    if user is None:
        raise UNAUTHORIZED_EXCEPTION

    return user
