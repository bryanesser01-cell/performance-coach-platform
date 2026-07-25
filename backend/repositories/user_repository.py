from sqlalchemy.orm import Session

from database.user_models import User
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[User]):
    """
    Repository responsible for all User database operations.
    """

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(
            User,
            db,
        )

    def get_by_email(
        self,
        email: str,
    ) -> User | None:
        """
        Retrieve a user by email address.
        """
        return self.db.query(User).filter(User.email == email).first()
