from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from common.db_model import BaseModel

Base = declarative_base()

class AssistantModel(BaseModel):
    __tablename__ = 'assistant'

    title = Column(String, index=True)
    model = Column(String, index=True)
    prompt = Column(String, index=True, nullable=True)