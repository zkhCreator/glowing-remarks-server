from sqlalchemy import Column, String, Text

from common.db_model import BaseDBModel

class AssistantDBModel(BaseDBModel):
    __tablename__ = 'assistant'

    title = Column(String(255))
    model = Column(String(255))
    prompt = Column(Text, nullable=True)