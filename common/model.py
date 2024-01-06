from datetime import datetime
from typing import Any, Optional, Type, TypeVar
from uuid import UUID
from pydantic import BaseModel, Field


class EditableBaseModel(BaseModel):
    create_time: datetime = Field(
        default_factory=datetime.utcnow, alias='create_time', read_only=True)
    update_time: datetime = Field(
        default_factory=datetime.utcnow, alias='update_time', read_only=True)

ModelType = TypeVar('ModelType', bound='CommonBaseModel')
ORMType = TypeVar('ORMType')

class CommonBaseModel(BaseModel):
    @classmethod
    def from_orm(cls: Type[ModelType], orm_obj: ORMType) -> ModelType:
        return cls.model_validate(orm_obj.__dict__)

    def to_orm(self: ModelType) -> ORMType:
        return self.model_dump()