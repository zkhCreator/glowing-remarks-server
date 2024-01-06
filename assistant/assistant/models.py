from pydantic import Field
from typing import Optional
from uuid import UUID

from common.model import CommonBaseModel
from .db_models import AssistantDBModel
from datetime import datetime


class Assistant(CommonBaseModel):
    title: str
    model: str
    prompt: Optional[str] = None
    basic_language: Optional[str] = None
