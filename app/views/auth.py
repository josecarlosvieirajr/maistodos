import logging
from datetime import timedelta

from fastapi import APIRouter

from app.auth import Auth, Token, create_access_token
from app.config import settings

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/", response_model=Token)
async def auth(data: Auth):
    access_token_expires = timedelta(minutes=settings.token_expire)
    access_token = create_access_token(
        data={"sub": data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
