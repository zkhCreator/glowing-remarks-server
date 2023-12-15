
from assistant.assistant.db_models import AssistantDBModel
from assistant.assistant.models import Assistant
from assistant.user_assistant.db_model import UserAssistantDBModel

from auth.db_models import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.engine import Result

from common.pagination import PaginationListResponse, PaginationModel
from sqlalchemy import desc


async def assistant_list(user: User,  db: AsyncSession, pagination: PaginationModel):
    # Query for the ids of the UserAssistant objects
    result = await db.execute(select(UserAssistantDBModel.assistant_id).where(UserAssistantDBModel.user_id == user.id))
    user_assistant_ids = result.scalars().all()

    stmt = select(AssistantDBModel).where(AssistantDBModel.id.in_(user_assistant_ids)).order_by(desc(
        AssistantDBModel.update_time)).limit(pagination.page_size).offset((pagination.page_num) * pagination.page_size)
    
    assistant_result = await db.execute(stmt)
    assistants = assistant_result.scalars().all()
    
    # Count the total number of assistants for the user
    total_result: Result = await db.execute(select(func.count()).where(UserAssistantDBModel.user_id == user.id))
    total = total_result.scalar_one()

    return PaginationListResponse[Assistant](
        total=total,
        page_num=pagination.page_num,
        page_size=pagination.page_size,
        data=assistants
    )
