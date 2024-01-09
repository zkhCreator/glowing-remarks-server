from sqlalchemy import Column, String

from common.db_model import BaseDBModel
from sqlalchemy_utils import UUIDType


class ChatSessionDBModel(BaseDBModel):
    __tablename__ = 'chat_session'

    user_id = Column(UUIDType(binary=False), index=True)
    type = Column(String(64), nullable=False)
