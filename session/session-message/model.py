

from common.model import CommonBaseModel
from openai import OpenAI


class SessionMessageModel(CommonBaseModel):
    session_id: str
    role: str
    # 用户的内容
    message: str
