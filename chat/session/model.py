

from common.model import CommonBaseModel

class ChatSessionModel(CommonBaseModel):
    user_id: str
    # chat 对话形式, data 数据列表的形式
    type: str