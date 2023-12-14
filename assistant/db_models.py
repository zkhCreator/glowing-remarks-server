from sqlalchemy import Column, String, Text

from common.db_model import BaseModel

class AssistantDBModel(BaseModel):
    __tablename__ = 'assistant'

    title = Column(String(255))
    model = Column(String(255))
    prompt = Column(Text, nullable=True)