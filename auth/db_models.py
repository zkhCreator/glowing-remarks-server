from common.database import Base
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID

from fastapi import Depends
from common.database import get_async_session

from common.database import Base
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
