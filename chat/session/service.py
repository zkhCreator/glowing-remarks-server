from uuid import UUID
from sqlalchemy import Result, and_, desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from chat.session.db_model import ChatSessionDBModel
from common.pagination import PaginationListResponse, PaginationModel
from .model import ChatSessionModel


class ChatSessionService:
    @staticmethod
    async def get(id: UUID, userId: UUID, db: AsyncSession) -> ChatSessionModel:
        result = await db.execute(select(ChatSessionDBModel).where(and_(ChatSessionDBModel.id == id, ChatSessionDBModel.user_id == userId)))

        chat_session_exist = result.scalars().first()
        chat_session_model = ChatSessionModel.from_orm(chat_session_exist)

        return chat_session_model

    @staticmethod
    async def list(userId: UUID, db: AsyncSession, pagination: PaginationModel) -> [ChatSessionModel]:
        # Query for the ids of the UserAssistant objects
        result = await db.execute(select(ChatSessionDBModel.assistant_id).where(ChatSessionDBModel.user_id == userId))
        user_assistant_ids = result.scalars().all()

        stmt = select(ChatSessionDBModel).where(ChatSessionDBModel.id.in_(user_assistant_ids)).order_by(desc(
            ChatSessionDBModel.update_time)).limit(pagination.page_size).offset((pagination.page_num) * pagination.page_size)

        assistant_result = await db.execute(stmt)
        assistants = assistant_result.scalars().all()

        # Count the total number of assistants for the user
        total_result: Result = await db.execute(select(func.count()).where(ChatSessionDBModel.user_id == userId))
        total = total_result.scalar_one()

        return PaginationListResponse[ChatSessionModel](
            total=total,
            page_num=pagination.page_num,
            page_size=pagination.page_size,
            data=assistants
        )

    @staticmethod
    async def create(chat_session: ChatSessionModel, db: AsyncSession) -> ChatSessionModel:
        db_chat_session: ChatSessionDBModel = chat_session.to_orm[ChatSessionDBModel](
        )
        db.add(db_chat_session)

        await db.commit()
        await db.refresh(db_chat_session)

        return chat_session
