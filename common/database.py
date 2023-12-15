from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from common.setting import settings

class Base(DeclarativeBase):
    pass


DB_USER = settings.DB_USER
DB_PASSWORD = settings.DB_PASSWORD
DB_HOST = settings.DB_HOST
DB_NAME = settings.DB_NAME

DATABASE_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def on_startup():
    # Not needed if you setup a migration system like Alembic
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
