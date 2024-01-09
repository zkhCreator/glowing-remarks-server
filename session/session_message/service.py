from typing import Optional
from uuid import UUID
from sqlalchemy import and_, select

from common.pagination import PaginationModel
from .model import SessionMessageModel
from sqlalchemy.ext.asyncio import AsyncSession
from .db_model import SessionMessageDBModel


class SessionMessageService:
    @staticmethod
    async def add(sessionMessage: SessionMessageModel, db: AsyncSession) -> SessionMessageModel:
        db_session_message: SessionMessageDBModel = sessionMessage.to_orm[SessionMessageDBModel](
        )
        db.add(db_session_message)

        await db.commit()
        await db.refresh(db_session_message)
        return sessionMessage

    @staticmethod
    async def list(sessionId: UUID, db: AsyncSession, pagination: Optional[PaginationModel]) -> [SessionMessageDBModel]:
        query = select(SessionMessageDBModel).where(
            and_(SessionMessageDBModel.session_id == sessionId))

        if pagination:
            query = query.limit(pagination.page_size).offset(
                pagination.page_num * pagination.page_size)

        result = await db.execute(query)
        sessionMessages = result.scalars().all()
        return sessionMessages

    @staticmethod
    async def update(id: UUID, db: AsyncSession, new_text: str) -> SessionMessageDBModel:
        query = select(SessionMessageDBModel).where(
            SessionMessageDBModel.id == id)
        result = await db.execute(query)
        sessionMessage = result.scalars().first()
        sessionMessage.message = new_text
        await db.commit()
        await db.refresh(sessionMessage)

        return sessionMessage
