from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime
from .db_models import AssistantModel

class Assistant(BaseModel):
    id: Optional[UUID] = None
    title: str
    model: str
    prompt: Optional[str] = None
    createTime: Optional[datetime] = None
    updateTime: Optional[datetime] = None

    @classmethod
    def from_orm(cls, assistant_model: AssistantModel):
        return cls(**assistant_model.__dict__)

    def to_orm(self):
        return AssistantModel(**self.dict(exclude_unset=True))