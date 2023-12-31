from sqlalchemy import Boolean, Column, DateTime
from sqlalchemy.sql import func
from sqlalchemy_utils import UUIDType
import uuid

from common.database import Base

class BaseDBModel(Base):
    __abstract__ = True

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    
    create_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True),
                         server_default=func.now(), onupdate=func.now())

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key.lower() == 'id':
                continue  # Skip the 'id' field
            if hasattr(self, key):
                setattr(self, key, value)


class DeletableBaseDBModel(BaseDBModel):
    __abstract__ = True

    is_delete = Column(Boolean, nullable=False, default=False)
