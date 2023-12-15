from sqlalchemy import Column
from sqlalchemy_utils import UUIDType

from common.db_model import EditableDBBaseModel

class UserAssistantDBModel(EditableDBBaseModel):
    __tablename__ = 'user_assistant'

    user_id = Column(UUIDType(binary=False), primary_key=True, index=True)
    assistant_id = Column(UUIDType(binary=False), primary_key=True, index=True)
