from datetime import datetime, timedelta

from fastapi import Header, HTTPException, status
from jose import JWTError, jwt
from pydantic import BaseModel

from app.config import settings


class Token(BaseModel):
    access_token: str
    token_type: str


class Auth(BaseModel):
    username: str


def raise_exception():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"token": "Bearer"},
    )


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.secret_key, algorithm=settings.algorithm
    )
    return encoded_jwt


def check_token(token: str = Header()):
    payload: dict = {}
    try:
        payload = jwt.decode(
            token, settings.secret_key, algorithms=[settings.algorithm]
        )
    except JWTError:
        raise_exception()

    username = payload.get("sub", None)
    if username is None:
        raise_exception()

    return username
