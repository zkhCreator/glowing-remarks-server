from uuid import UUID
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from assistant.db_models import AssistantDBModel

from common.database import get_async_session

from sqlalchemy.sql import select


async def get_assistant(assistant_id: UUID, db: AsyncSession = Depends(get_async_session)) -> AssistantDBModel:
    result = await db.execute(select(AssistantDBModel).where(AssistantDBModel.id == assistant_id))
    assistant = result.scalars().first()
    if not assistant:
        raise HTTPException(status_code=404, detail="Assistant not found")
    return assistant
