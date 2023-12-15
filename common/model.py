from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class EditableBaseModel(BaseModel):
    createTime: datetime = Field(
        default_factory=datetime.utcnow, alias='createTime', read_only=True)
    updateTime: datetime = Field(
        default_factory=datetime.utcnow, alias='updateTime', read_only=True)


class CommonBaseModel(EditableBaseModel):
    id: Optional[UUID] = None
    createTime: datetime = Field(
        default_factory=datetime.utcnow, alias='createTime', read_only=True)
    updateTime: datetime = Field(
        default_factory=datetime.utcnow, alias='updateTime', read_only=True)
