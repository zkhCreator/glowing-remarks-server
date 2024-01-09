

from enum import Enum
from uuid import UUID
from chat.session.db_model import ChatSessionDBModel
from common.model import EditableBaseModel


class ChatType(Enum):
    chat = "chat"
    data = "data"
    
    def __str__(self) -> str:
        return self.name


class ChatSessionModel(EditableBaseModel):
    user_id: UUID
    # chat 对话形式, data 数据列表的形式
    type: str

