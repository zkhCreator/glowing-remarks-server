

from common.model import CommonBaseModel
from openai import OpenAI




class ChatMessage(CommonBaseModel):
    user_id: str
    assistant_id: str
    # 用户的内容
    message: str

    # 请求 openAI 配置的参数
    params: str

    # response openAI 返回的结果
    response: str
