from typing import Optional
from uuid import UUID
from sqlalchemy import Result, and_, desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from .db_model import SessionDBModel
from common.pagination import PaginationListResponse, PaginationModel
from .model import SessionCreateModel, SessionDeleteModel, SessionReadModel


class SessionService:
    @staticmethod
    async def get(id: UUID, userId: UUID, db: AsyncSession) -> Optional[SessionReadModel]:
        result = await db.execute(select(SessionDBModel).where(and_(SessionDBModel.id == id, SessionDBModel.user_id == userId, SessionDBModel.is_delete == False)))

        chat_session_exist = result.scalars().first()
        if (chat_session_exist is None):
            return None
        chat_session_model = SessionReadModel.from_orm(chat_session_exist)
        # .from_orm(chat_session_exist)

        return chat_session_model

    @staticmethod
    async def create(chat_session: SessionCreateModel, db: AsyncSession) -> SessionReadModel:
        db_chat_session: SessionDBModel = chat_session.to_orm()

        print(vars(db_chat_session))
        db.add(db_chat_session)

        await db.commit()
        await db.refresh(db_chat_session)
        print(vars(db_chat_session))
        return SessionReadModel.from_orm(db_chat_session)

    @staticmethod
    async def delete(session: SessionDeleteModel, user_id: UUID, db: AsyncSession):
        try:
            result = await db.execute(select(SessionDBModel)
                                      .where(and_(SessionDBModel.id == session.id,
                                                  SessionDBModel.user_id == session.user_id,
                                                  SessionDBModel.is_delete == False,
                                                  SessionDBModel.type == session.type,
                                                  SessionDBModel.user_id == user_id)))
            chat_session_exist = result.scalars().first()
            if (chat_session_exist is None):
                return None
            chat_session_exist.is_delete = True
            # how to save data
            await db.commit()
            await db.refresh(chat_session_exist)

            return SessionReadModel.from_orm(chat_session_exist)
        except NoResultFound:
            return None

    @staticmethod
    async def list(userId: UUID, db: AsyncSession, pagination: PaginationModel) -> [SessionReadModel]:
        # Query for the ids of the UserAssistant objects
        result = await db.execute(select(SessionDBModel.assistant_id).where(SessionDBModel.user_id == userId))
        user_assistant_ids = result.scalars().all()

        stmt = select(SessionDBModel).where(SessionDBModel.id.in_(user_assistant_ids)).order_by(desc(
            SessionDBModel.update_time)).limit(pagination.page_size).offset((pagination.page_num) * pagination.page_size)

        assistant_result = await db.execute(stmt)
        assistants = assistant_result.scalars().all()

        # Count the total number of assistants for the user
        total_result: Result = await db.execute(select(func.count()).where(SessionDBModel.user_id == userId))
        total = total_result.scalar_one()

        return PaginationListResponse[SessionReadModel](
            total=total,
            page_num=pagination.page_num,
            page_size=pagination.page_size,
            data=assistants
        )
