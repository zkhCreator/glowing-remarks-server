from sqlalchemy import JSON

from common.db_model import BaseDBModel


class TaskItemDBModel(BaseDBModel):
    
    __tablename__ = "task_item"
    
    title: str
    type: str   # table, calendar
    