import logging
from typing import List

from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session

from app.db.model import CreditCard, engine
from app.db.repository import credit_card_repository
from app.db.schema import CreditCardSchema

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/", response_model=List[CreditCard])
async def list_all_credit_card(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        resp = credit_card_repository.get_multi(session, skip=skip, limit=limit)
    return resp


@router.get("/{id}", response_model=CreditCard)
async def get_credit_card_for_key(id: int):
    with Session(engine) as session:
        resp = credit_card_repository.get(session, id=id)
    return resp


@router.post("/", status_code=status.HTTP_200_OK)
async def create_credit(data: CreditCardSchema):
    with Session(engine) as session:
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
