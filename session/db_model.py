from sqlalchemy import Boolean, Column, String

from common.db_model import BaseDBModel
from sqlalchemy_utils import UUIDType


class SessionDBModel(BaseDBModel):
    __tablename__ = 'session'

    user_id = Column(UUIDType(binary=False), index=True)
    type = Column(String(64), nullable=False)
    is_delete = Column(Boolean, nullable=False, default=False)
