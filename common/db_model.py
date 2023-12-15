from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from sqlalchemy_utils import UUIDType
import uuid

from common.database import Base

class EditableDBBaseModel(Base):
    __abstract__ = True

    createTime = Column(DateTime(timezone=True), server_default=func.now())
    updateTime = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class BaseDBModel(EditableDBBaseModel):
    __abstract__ = True

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key.lower() == 'id':
                continue  # Skip the 'id' field
            if hasattr(self, key):
                setattr(self, key, value)
            