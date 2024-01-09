from typing import Optional
from uuid import UUID
from sqlalchemy import Result, and_, desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from .db_model import SessionDBModel
from common.pagination import PaginationListResponse, PaginationModel
from .model import SessionCreateModel, SessionDeleteModel, SessionReadModel

from .session_message.service import SessionMessageService
from .session_message.model import SessionMessageModel


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

        db.add(db_chat_session)

        await db.commit()
        await db.refresh(db_chat_session)
        return SessionReadModel.from_orm(db_chat_session)

    @staticmethod
    async def delete(session: SessionDeleteModel, user_id: UUID, db: AsyncSession):
        print(vars(session))
        print(user_id)
        try:
            result = await db.execute(select(SessionDBModel)
                                      .where(and_(SessionDBModel.id == session.id,
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
    async def messageList(session_id: UUID, db: AsyncSession, pagination: Optional[PaginationModel] = None):

        query = select(SessionMessageModel).where(
            SessionMessageModel.session_id == session_id)

        if pagination is not None:
            query = pagination.paginate(query)

        result = await db.execute(query)
        session_message_list = result.scalars().all()

        return [SessionMessageModel.from_orm(session_message) for session_message in session_message_list]

    @staticmethod
    async def appendMessage(session_id: UUID, message: str, role: str, db: AsyncSession):
        # 调用 Message 的 服务处理
        session_message = SessionMessageModel(
            session_id=session_id, message=message, role=role)
        saved_message = await SessionMessageService.add(session_message, db)
        return saved_message
