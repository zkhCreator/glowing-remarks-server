from typing import Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status

from auth.users import current_active_user_id
from chat.model import SendMessageModel
from chat.session.model import ChatSessionModel, ChatType
from chat.session.service import ChatSessionService
from common.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/completion", description="聊天用的接口")
async def completion(message: SendMessageModel, user_id: UUID = Depends(current_active_user_id), db: AsyncSession = Depends(get_async_session)):
    session_id = message.session_id
    message_str = message.message

    session = None
    if session_id is None:
        session_model = ChatSessionModel(user_id=user_id, type=ChatType.chat)
        session = await ChatSessionService.create(session_model, db=db)
    else:
        session = await ChatSessionService.get(session_id, userId=user_id, db=db)
        if session is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Data not found")

    return {"session": session}
