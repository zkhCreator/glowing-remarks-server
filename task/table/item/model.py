from dataclasses import dataclass
from uuid import UUID
from common.model import CommonBaseModel
from .db_model import UserUsageTokenDBModel


class TaskTableItemModel(CommonBaseModel):
    table_id: UUID
    
    data: dict
