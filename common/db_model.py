from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy_utils import UUIDType
import uuid

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    createTime = Column(DateTime(timezone=True), server_default=func.now())
    updateTime = Column(DateTime(timezone=True), onupdate=func.now())