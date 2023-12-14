
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID

from common.database import Base
from sqlalchemy import Column, String, Date


class User(SQLAlchemyBaseUserTableUUID, Base):
    first_name = Column(String(256), nullable=False)
    birthdate = Column(Date, nullable=True)