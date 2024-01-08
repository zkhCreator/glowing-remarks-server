from sqlalchemy import Column, String, Text

from common.db_model import BaseDBModel
from sqlalchemy_utils import UUIDType
from sqlalchemy.dialects.mysql import TEXT


class ChatSessionDBModel(BaseDBModel):
    __tablename__ = 'chat_session_message'

    session_id = Column(UUIDType(binary=False), index=True)
    role = Column(Column(String(255), nullable=False))
    message = Column(TEXT, nullable=False)
