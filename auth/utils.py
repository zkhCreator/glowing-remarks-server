from jose import jwt
from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2AuthorizationCodeBearer
from starlette.status import HTTP_403_FORBIDDEN

from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator
from common.database import async_session_maker
from fastapi_users.authentication import (
    BearerTransport,
)

credentials_exception = HTTPException(
    status_code=401,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

oauth2_scheme = OAuth2AuthorizationCodeBearer(authorizationUrl="/auth/authorize",
                                              tokenUrl="/auth/token"
                                              )
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

SECRET = "SECRET"


def authenticate_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, "YOUR_SECRET_KEY", algorithms=["HS256"])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        return email
    except jwt.JWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
