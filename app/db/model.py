from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel, create_engine

from app.config import settings


class Base(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow(), index=True)
    updated_at: datetime = Field(default=datetime.utcnow(), index=True)


class CreditCardBase(SQLModel):
    holder: str = Field(index=True)
    number: str = Field(unique=True)
    exp_date: str
    cvv: Optional[int] = None


class CreditCard(Base, CreditCardBase, table=True):
    brand: str = Field(index=True)


connect_args = {"check_same_thread": False}
engine = create_engine(settings.database_url, echo=True, connect_args=connect_args)
