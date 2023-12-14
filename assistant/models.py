from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from .db_models import AssistantDBModel
from datetime import datetime


class Assistant(BaseModel):
    id: Optional[UUID] = None
    title: str
    model: str
    prompt: Optional[str] = None
    createTime: datetime = Field(
        default_factory=datetime.utcnow, alias='createTime', read_only=True)
    updateTime: datetime = Field(
        default_factory=datetime.utcnow, alias='updateTime', read_only=True)

    @classmethod
    def from_orm(cls, assistant_model: AssistantDBModel):
        return cls(**assistant_model.__dict__)

    def to_orm(self):
        return AssistantDBModel(**self.model_dump(exclude_unset=True))
