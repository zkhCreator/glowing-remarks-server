from sqlalchemy import JSON, TEXT, Column, Integer
from common.db_model import BaseDBModel
from sqlalchemy_utils import UUIDType


class TaskTableItemDBModel(BaseDBModel):
    __tablename__ = 'task_table_item'

    # 关联的表名称
    table_id: Column(UUIDType, nullable=False)

    # 序列化的数据
    data = Column(JSON, nullable=False)

    # 是否删除
    is_deleted = Column(Integer, nullable=False, default=0)
