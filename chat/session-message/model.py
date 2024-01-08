

from common.model import CommonBaseModel
from openai import OpenAI


class ChatMessageModel(CommonBaseModel):
    session_id: str
    role: str
    # 用户的内容
    message: str
