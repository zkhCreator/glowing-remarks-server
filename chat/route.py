from typing import Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status

from auth.users import current_active_user_id
from chat.model import SendMessageModel
from session.model import SessionCreateModel, SessionDeleteModel, SessionReadModel, SessionType
from session.service import SessionService
from common.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/completion", description="聊天用的接口")
async def completion(message: SendMessageModel, user_id: UUID = Depends(current_active_user_id), db: AsyncSession = Depends(get_async_session)):
    session_id = message.session_id
    message_str = message.message

    print("-------------")
    session = None
    if session_id is None:
        print(user_id)
        session_model = SessionCreateModel(
            user_id=user_id, type=SessionType.chat)
        print(session_model.dict())
        session = await SessionService.create(session_model, db=db)
    else:
        session = await SessionService.get(session_id, userId=user_id, db=db)
        if session is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Data not found")

    return {"session": session}


@router.delete("/delete", description="删除某一个 session")
async def deleteSession(session: SessionDeleteModel, user_id: UUID = Depends(current_active_user_id), db: AsyncSession = Depends(get_async_session)):
    deleted_session = await SessionService.delete(session, user_id, db)

    if not deleted_session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Data not found")

    return deleted_session
