from pydantic import validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str
    SECRET_KEY: str

    @classmethod
    @validator("DB_USER", "DB_HOST", "DB_NAME", "SECRET_KEY")
    def check_not_empty(cls, v):
        assert v != "", f"{v} is not defined"
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
