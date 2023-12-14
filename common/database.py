from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine

load_dotenv()

Base = declarative_base()


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def startup():
    Base.metadata.create_all(bind=engine)
    pass


async def shutdown():
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()