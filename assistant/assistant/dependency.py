from uuid import UUID
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from auth.db_models import User
from .db_models import AssistantDBModel
from common.database import get_async_session
from sqlalchemy.sql import select
from auth.users import current_active_user
from assistant.user_assistant.db_model import UserAssistantDBModel
from sqlalchemy.sql import exists

async def get_assistant(assistant_id: UUID, user: User = Depends(current_active_user), db: AsyncSession = Depends(get_async_session)):
    user_assistant_exists = await db.execute(
        select(exists().where(UserAssistantDBModel.user_id == user.id).where(UserAssistantDBModel.assistant_id == assistant_id))
    )

    if not user_assistant_exists.scalar():
        raise HTTPException(status_code=404, detail="Assistant not found")
    
    result = await db.execute(select(AssistantDBModel).where(AssistantDBModel.id == assistant_id))
    assistant = result.scalars().first()
    if not assistant:
        raise HTTPException(status_code=404, detail="Assistant not found")
    return assistant
