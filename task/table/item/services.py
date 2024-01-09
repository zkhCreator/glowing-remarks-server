from typing import Optional
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from common.pagination import PaginationModel
from task.table.item.db_model import TaskTableItemDBModel
from task.table.item.model import TaskTableItemModel


class TaskTableItemService:
    @staticmethod
    async def list(table_id: UUID, db: AsyncSession, pagination: Optional[PaginationModel]) -> [TaskTableItemModel]:
        query = select(TaskTableItemDBModel).where(
            TaskTableItemDBModel.table_id == table_id)

        if (pagination):
            query = pagination.paginate(query)

        result = await db.execute(query)
        result_model = TaskTableItemModel.from_orm_list(result)

        return result_model

    @staticmethod
    async def add(new_model: TaskTableItemModel, db: AsyncSession):
        db_model = new_model.to_orm[TaskTableItemDBModel]()

        db.add(db_model)
        await db.commit()
        await db.refresh(db_model)

        return new_model

    async def delete(id: UUID, db: AsyncSession):
        result = await db.execute(
            select(TaskTableItemDBModel).where(
                TaskTableItemDBModel.id == id
            )
        )

        db_model = result.fetchone()[0]
        db_model.delete = True

        db.delete(db_model)
        await db.commit(db_model)
        await db.refresh(db_model)

        return db_model
