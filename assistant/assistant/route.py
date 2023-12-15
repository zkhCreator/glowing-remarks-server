from fastapi import APIRouter, Depends, HTTPException, status
from assistant.user_assistant.db_model import UserAssistantDBModel

from auth.db_models import User

from .dependency import get_assistant
from .models import Assistant
from common.database import get_async_session
from .db_models import AssistantDBModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select, delete
from auth.users import current_active_user

router = APIRouter(prefix="/assistant", tags=["assistant"])


@router.post("/")
async def create_assistant(assistant: Assistant, user: User = Depends(current_active_user), db: AsyncSession = Depends(get_async_session)):
    db_assistant = assistant.to_orm()

    db.add(db_assistant)
    await db.commit()
    await db.refresh(db_assistant)

    try:
        user_assistant = UserAssistantDBModel(
            user_id=user.id, assistant_id=db_assistant.id)
        db.add(user_assistant)
        await db.commit()
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return db_assistant


@router.get("/{assistant_id}")
async def read_assistant(assistant: AssistantDBModel = Depends(get_assistant)):
    assistant_model = Assistant.from_orm(assistant)
    assistant_model.createTime = assistant.createTime
    assistant_model.updateTime = assistant.updateTime

    return assistant_model


@router.put("/{assistant_id}")
async def update_assistant(assistant: Assistant, assistant_db: AssistantDBModel = Depends(get_assistant), db: AsyncSession = Depends(get_async_session)):
    assistant_db.update(**assistant.model_dump(exclude_unset=True))
    await db.commit()

    # Re-fetch the assistant after updating
    result = await db.execute(select(AssistantDBModel).where(AssistantDBModel.id == assistant_db.id))
    db_assistant = result.scalars().first()

    return db_assistant


@router.delete("/{assistant_id}")
async def delete_assistant(assistant_db: AssistantDBModel = Depends(get_assistant), db: AsyncSession = Depends(get_async_session)):
    await db.execute(
        delete(AssistantDBModel).
        where(AssistantDBModel.id == assistant_db.id)
    )
    await db.commit()
    return {"message": "Assistant deleted"}
