import datetime
from uuid import UUID
from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession

from .db_model import UserUsageTokenDBModel

from .model import UserUsageTokenModel
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select


class UsageService:
    @staticmethod
    async def addUsage(usage: UserUsageTokenModel, db: AsyncSession):
        db_usage: UserUsageTokenDBModel = usage.to_orm[UserUsageTokenDBModel]()
        db.add(db_usage)
        
        await db.commit()

    @staticmethod
    async def userUsage(userId: UUID, db: AsyncSession, startTime: datetime, endTime: datetime):
        result = await db.execute(
            select(UserUsageTokenDBModel).where(
                and_(
                    UserUsageTokenDBModel.user_id == userId,
                    UserUsageTokenDBModel.create_time >= startTime,
                    UserUsageTokenDBModel.create_time <= endTime
                )
            )
        )
        
        user_usage_exist = result.fetchall()
        user_usage_models = [UserUsageTokenModel.from_orm(item) for item in user_usage_exist]
        return user_usage_models
