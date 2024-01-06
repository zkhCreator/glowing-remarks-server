from sqlalchemy import TEXT, Column, Integer
from common.db_model import BaseDBModel
from sqlalchemy_utils import UUIDType


class UserUsageTokenDBModel(BaseDBModel):
    __tablename__ = 'user_usage'
    
    user_id = Column(UUIDType(binary=False), primary_key=True, index=True)
    request_message = Column(TEXT, nullable=False)
    response_message = Column(TEXT, nullable=False)
    request_token = request_token = Column(Integer, nullable=False)
    response_token = request_token = Column(Integer, nullable=False)
    