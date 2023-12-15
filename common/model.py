from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class EditableBaseModel(BaseModel):
    create_time: datetime = Field(
        default_factory=datetime.utcnow, alias='create_time', read_only=True)
    update_time: datetime = Field(
        default_factory=datetime.utcnow, alias='update_time', read_only=True)


class CommonBaseModel(EditableBaseModel):
    id: Optional[UUID] = None
