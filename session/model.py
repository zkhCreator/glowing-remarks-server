

from enum import Enum
from uuid import UUID
from common.model import CommonBaseModel, EditableBaseModel
from session.db_model import SessionDBModel


class SessionType(Enum):
    chat = "chat"
    data = "data"

    def __str__(self) -> str:
        return self.name

class SessionCreateModel(CommonBaseModel):
    user_id: UUID
    # chat 对话形式, data 数据列表的形式
    type: str

    def to_orm(self) -> SessionDBModel:
        return SessionDBModel(**self.model_dump())


class SessionReadModel(EditableBaseModel):
    user_id: UUID
    # chat 对话形式, data 数据列表的形式
    type: str


class SessionModel(SessionReadModel):
    is_delete: bool = False


class SessionDeleteModel(CommonBaseModel):
    id: UUID
    # chat 对话形式, data 数据列表的形式
    type: str
