from typing import List
from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from openai_layer.service import OpenAIService

from session.model import SessionCreateModel, SessionReadModel, SessionType
from session.service import SessionService
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam, ChatCompletionUserMessageParam


class ChatService:
    @staticmethod
    async def _getSession(session_id: UUID, user_id: UUID, db: AsyncSession):
        session = None
        if session_id is None:
            session_model = SessionCreateModel(
                user_id=user_id, type=SessionType.chat)
            session = await SessionService.create(session_model, db=db)
        else:
            session = await SessionService.get(session_id, userId=user_id, db=db)
            if session is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail="Data not found")
        return session

    @staticmethod
    async def _sendMessage(session: SessionReadModel,
                           originMessageList: List[ChatCompletionMessageParam],
                           message: str,
                           db: AsyncSession):
        originMessageList.append(
            {"role": "user", "content": message})
        completion = await OpenAIService.chat_completion(
            user_id=session.user_id, messages=originMessageList, db=db)

        return completion

    @staticmethod
    async def _saveMessage(session: SessionReadModel, message: str, receiveMessage: str, db: AsyncSession):
        await SessionService.appendMessage(session.id, message, "user", db)
        await SessionService.appendMessage(session.id, receiveMessage, "assistant", db)

    @staticmethod
    async def sendMessage(session_id: UUID, message: str, user_id: UUID, db: AsyncSession):
        session = await ChatService._getSession(session_id, user_id, db)
        # TODO: send Message 保存内容
        response = await ChatService._sendMessage(
            session, originMessageList=[], message=message, db=db)
        await ChatService._saveMessage(session, message, response, db)

        return {"status": session}
