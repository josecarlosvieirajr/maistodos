import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.auth import check_token
from app.db.model import CreditCard, get_session
from app.db.repository import credit_card_repository
from app.db.schema import CreditCardSchema, CreditCardSchemaUpdate

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/", response_model=List[CreditCard])
async def list_all_credit_card(
    *,
    session: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 100,
    username: str = Depends(check_token)
):
    resp = credit_card_repository.get_multi(session, skip=skip, limit=limit)
    return resp


@router.get("/{id}", response_model=CreditCard)
async def get_credit_card_for_key(
    id: int,
    *,
    session: Session = Depends(get_session),
    username: str = Depends(check_token)
):
    resp = credit_card_repository.get(session, id=id)
    return resp


@router.post("/", status_code=status.HTTP_200_OK)
async def create_credit(
    *,
    session: Session = Depends(get_session),
    data: CreditCardSchema,
    username: str = Depends(check_token)
):
    try:
        resp = credit_card_repository.create(session, obj_in=data)
        return resp
    except Exception as e:
        session.rollback()
        if list(filter(lambda x: "IntegrityError" in x, e.args)):
            raise HTTPException(
                status_code=409, detail="this card number already exists"
            )
        raise e


@router.put("/{id}", response_model=CreditCard)
async def update_credit_card_for_key(
    id: int,
    *,
    data: CreditCardSchemaUpdate,
    session: Session = Depends(get_session),
    username: str = Depends(check_token)
):
    resp = credit_card_repository.update(session, id=id, obj_in=data)
    return resp


@router.delete("/{id}", response_model=CreditCard)
async def delete_credit_card_for_key(
    id: int,
    *,
    session: Session = Depends(get_session),
    username: str = Depends(check_token)
):
    resp = credit_card_repository.remove(session, id=id)
    return resp
