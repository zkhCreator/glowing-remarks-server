from fastapi import APIRouter, Depends, HTTPException, Query, status
from assistant.user_assistant.db_model import UserAssistantDBModel
from assistant.user_assistant.list import assistant_list

from auth.db_models import User
from common.pagination import PaginationModel

from .assistant.dependency import get_assistant
from .assistant.models import Assistant
from common.database import get_async_session
from .assistant.db_models import AssistantDBModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select, delete
from auth.users import current_active_user
from fastapi.logger import logger

router = APIRouter(prefix="/assistant", tags=["assistant"])

@router.get("/list")
async def list(page_num: int = Query(0, alias="page_num"), 
               page_size: int = Query(20, alias="page_size"), 
               user: User = Depends(current_active_user), 
               db: AsyncSession = Depends(get_async_session)):
    pagination = PaginationModel(page_num=page_num, page_size=page_size)
    return await assistant_list(pagination=pagination, user=user, db=db)

@router.post("/create")
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

@router.get("/detail/{assistant_id}")
async def read_assistant(assistant: AssistantDBModel = Depends(get_assistant)):
    assistant_model = Assistant.from_orm(assistant)
    assistant_model.create_time = assistant.create_time
    assistant_model.update_time = assistant.update_time

    return assistant_model

@router.put("/update/{assistant_id}")
async def update_assistant(assistant: Assistant, assistant_db: AssistantDBModel = Depends(get_assistant), db: AsyncSession = Depends(get_async_session)):
    assistant_db.update(**assistant.model_dump(exclude_unset=True))
    await db.commit()

    # Re-fetch the assistant after updating
    result = await db.execute(select(AssistantDBModel).where(AssistantDBModel.id == assistant_db.id))
    db_assistant = result.scalars().first()

    return db_assistant


@router.delete("/update/{assistant_id}")
async def delete_assistant(assistant_db: AssistantDBModel = Depends(get_assistant), db: AsyncSession = Depends(get_async_session)):
    await db.execute(
        delete(AssistantDBModel).
        where(AssistantDBModel.id == assistant_db.id)
    )
    await db.commit()
    return {"message": "Assistant deleted"}



