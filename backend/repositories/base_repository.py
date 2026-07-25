from typing import Any, Generic, TypeVar

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    """
    Base repository containing common CRUD operations.
    """

    def __init__(
        self,
        model: type[ModelType],
        db: Session,
    ):
        self.model = model
        self.db = db

    def get_by_id(
        self,
        entity_id: int,
    ) -> ModelType | None:
        return self.db.get(
            self.model,
            entity_id,
        )

    def get_all(
        self,
    ) -> list[ModelType]:
        return self.db.query(
            self.model,
        ).all()

    def create(
        self,
        entity: ModelType,
    ) -> ModelType:
        self.db.add(
            entity,
        )
        self.db.commit()
        self.db.refresh(
            entity,
        )

        return entity

    def update(
        self,
        entity: ModelType,
        updates: dict[str, Any],
    ) -> ModelType:
        for field, value in updates.items():
            if not hasattr(
                entity,
                field,
            ):
                raise AttributeError(
                    f"{field} is not a valid field for {self.model.__name__}."
                )

            setattr(
                entity,
                field,
                value,
            )

        self.db.commit()
        self.db.refresh(
            entity,
        )

        return entity

    def delete(
        self,
        entity: ModelType,
    ) -> None:
        self.db.delete(
            entity,
        )
        self.db.commit()

    def flush(
        self,
    ) -> None:
        self.db.flush()

    def commit(
        self,
    ) -> None:
        self.db.commit()

    def rollback(
        self,
    ) -> None:
        self.db.rollback()
