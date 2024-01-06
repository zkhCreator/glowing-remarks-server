from dataclasses import dataclass
from uuid import UUID
from common.model import CommonBaseModel
from .db_model import UserUsageTokenDBModel


@dataclass
class UsageTokenModel():
    content: str
    token: int
class UserUsageTokenModel(CommonBaseModel):
    user_id: UUID
    request_message: str
    response_message: str
    request_token: int
    response_token: int