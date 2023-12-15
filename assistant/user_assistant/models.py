from typing import Optional
from assistant.assistant.db_models import AssistantDBModel

from common.model import CommonBaseModel

class UserAssistant(CommonBaseModel):
    title: str
    model: str
    prompt: Optional[str] = None

    @classmethod
    def from_orm(cls, assistant_model: AssistantDBModel):
        return cls(**assistant_model.__dict__)

    def to_orm(self):
        return AssistantDBModel(**self.model_dump(exclude_unset=True))
