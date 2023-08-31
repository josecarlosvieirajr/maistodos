from typing import Annotated, Optional

from creditcard import CreditCard
from pydantic import BaseModel, Field, root_validator, validator

from app.utils import datetime_validator, hashable


class CreditCardSchema(BaseModel):
    holder: str
    number: str
    exp_date: str
    cvv: Optional[int] = None
    brand: Optional[Annotated[str, Field(validate_default=True, hidden=True)]] = None

    @root_validator(pre=True)
    @classmethod
    def check_card_number(cls, values) -> str:
        number = values.get("number")
        cc = CreditCard(number)
        if not cc.is_valid():
            raise ValueError("Invalid card number")
        values["brand"] = cc.get_brand()
        values["number"] = hashable(number)
        return values

    @validator("exp_date", pre=True, always=True)
    @classmethod
    def check_valid_date(cls, value: str) -> str:
        return datetime_validator(value)

    @validator("cvv", pre=True, always=True)
    @classmethod
    def check_cvv(cls, value: int) -> int | None:
        if not value:
            return None

        if isinstance(value, int) and 3 <= len(str(value)) <= 4:
            return value
        raise ValueError("Invalid cvv")

    @validator("holder", pre=True, always=True)
    @classmethod
    def check_holder(cls, value: str) -> str:
        if isinstance(value, str) and len(value) > 2:
            return value
        raise ValueError("Invalid holder, very short statement")

    class Config:
        orm_mode = True
