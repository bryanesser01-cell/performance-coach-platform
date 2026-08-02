from typing import Generic, Type, TypeVar

from sqlalchemy.orm import Session

from database.base import Base

ModelType = TypeVar(
    "ModelType",
    bound=Base,
)


class BaseRepository(Generic[ModelType]):
    """
    Generic repository providing common database operations.
    """

    def __init__(
        self,
        db: Session,
        model: Type[ModelType],
    ):
        self.db = db
        self.model = model

    def get_by_id(
        self,
        record_id: int,
    ) -> ModelType | None:
        """
        Retrieve a record by primary key.
        """

        return self.db.query(self.model).filter(self.model.id == record_id).first()

    def get_all(
        self,
    ) -> list[ModelType]:
        """
        Retrieve all records.
        """

        return self.db.query(self.model).all()

    def delete(
        self,
        record: ModelType,
    ) -> None:
        """
        Delete a record.
        """

        self.db.delete(record)
        self.db.commit()
