from sqlalchemy import Column, String, Text

from common.db_model import BaseDBModel
from sqlalchemy_utils import UUIDType
from sqlalchemy.dialects.mysql import TEXT

class ChatSessionDBModel(BaseDBModel):
    __tablename__ = 'chat_session'

    user_id = Column(UUIDType(binary=False), index=True)
    assistant_id = Column(UUIDType(binary=False), index=True)
    message = Column(TEXT, nullable=False)
    params = Column(TEXT, nullable=False)
    response = Column(TEXT, nullable=False)