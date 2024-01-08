from sqlalchemy import Column

from common.db_model import BaseDBModel
from sqlalchemy_utils import UUIDType


class ChatSessionDBModel(BaseDBModel):
    __tablename__ = 'chat_session'

    user_id = Column(UUIDType(binary=False), index=True)
    