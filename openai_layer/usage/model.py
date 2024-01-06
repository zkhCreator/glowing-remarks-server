from common.model import CommonBaseModel
from .db_model import UserUsageTokenDBModel


class UserUsageTokenModel(CommonBaseModel):
    request_message: str
    response_message: str
    request_token: int
    response_token: int