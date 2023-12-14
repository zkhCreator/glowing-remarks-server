from jose import jwt
from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2AuthorizationCodeBearer
from starlette.status import HTTP_403_FORBIDDEN

from fastapi import HTTPException

credentials_exception = HTTPException(
    status_code=401, 
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="tokenUrl")

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