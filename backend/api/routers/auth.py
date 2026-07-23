from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.auth_service import register_user
from database.database import get_db
from schemas.user_schema import UserCreate, UserResponse

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return register_user(db, user)