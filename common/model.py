from datetime import datetime
from typing import Any, Optional, Type, TypeVar
from uuid import UUID
from pydantic import BaseModel, Field


ModelType = TypeVar('ModelType', bound='CommonBaseModel')
ORMType = TypeVar('ORMType')


class CommonBaseModel(BaseModel):
    @classmethod
    def from_orm(cls: Type[ModelType], orm_obj: ORMType) -> ModelType:
        return cls(**vars(orm_obj))

    def to_orm(self: ModelType) -> ORMType:
        return ORMType(**self.model_dump())

    @classmethod
    def from_orm_list(cls: Type[ModelType], orm_obj: [ORMType]) -> [ModelType]:
        return [cls.from_orm(item) for item in orm_obj]


class EditableBaseModel(CommonBaseModel):
    id: UUID = Field(alias='id', read_only=True)
    create_time: datetime = Field(
        default_factory=datetime.utcnow, alias='create_time', read_only=True)
    update_time: datetime = Field(
        default_factory=datetime.utcnow, alias='update_time', read_only=True)
