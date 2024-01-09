
from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


@dataclass
class SendMessageModel(BaseModel):
    message: str
    session_id: Optional[UUID] = None
