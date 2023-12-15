from typing import Optional
from assistant.assistant.db_models import AssistantDBModel

from common.model import EditableBaseModel

class UserAssistant(EditableBaseModel):
    user_id: str
    assistant_id: str

    @classmethod
    def from_orm(cls, assistant_model: AssistantDBModel):
        return cls(**assistant_model.__dict__)

    def to_orm(self):
        return AssistantDBModel(**self.model_dump(exclude_unset=True))
