
from fastapi import APIRouter
from auth.users import current_active_user
from assistant.assistant.dependency import get_assistant

router = APIRouter(prefix=["chat"], tags=["chat"], dependencies=[current_active_user, get_assistant])

@router.post("/create")
async def create_chat_message():
    pass