"""
## Modulo de Schemas, a camada de serialização e validação de dados.
"""
from typing import Annotated, Optional

from creditcard import CreditCard
from pydantic import BaseModel, Field, root_validator, validator

from app.utils import datetime_validator, hashable


class CreditCardSchemaUpdate(BaseModel):
    """
    Esquema de atualização para informações de cartão de crédito.

    Esta classe define o esquema de validação para a atualização de informações do titular de um cartão de crédito.

    **Atributos**

    * `holder` (str): O novo nome do titular do cartão.

    **Métodos Estáticos**

    * `check_holder(cls, value: str) -> str`: Valida o novo nome do titular do cartão.

    **Validação de Titular**

    O método `check_holder` valida o novo nome do titular do cartão, garantindo que ele tenha
    mais de 2 caracteres.

    Args:
        holder (str): O novo nome do titular do cartão.

    Returns:
        value (str): O novo nome do titular validado.

    Raises:
        ValueError: Se o novo nome do titular for muito curto.
    """

    holder: str

    @validator("holder", pre=True, always=True)
    @classmethod
    def check_holder(cls, value: str) -> str:
        """
        Valida o nome do titular do cartão.

        Args:
            value (str): O nome do titular do cartão.

        Returns:
            str: O nome do titular validado.

        Raises:
            ValueError: Se o nome do titular for muito curto.
        """
        if isinstance(value, str) and 2 < len(value) < 100:
            return value
        raise ValueError(
            "Holder name must be more than 2 characters and less than 100 characters"
        )


class CreditCardSchema(BaseModel):
    """
    Esquema de validação para informações de cartão de crédito.

    Esta classe define o esquema de validação para informações de cartão de crédito,
    incluindo o titular, número, data de expiração e CVV. Além disso, contém validações
    personalizadas para o número do cartão, data de expiração, CVV e titular.

    **Atributos**

    * `holder` (str): O nome do titular do cartão.
    * `number` (str): O número do cartão de crédito.
    * `exp_date` (str): A data de expiração do cartão (no formato "mm/aaaa").
    * `cvv` (Optional[int]): O código CVV do cartão (opcional).
    * `brand` (Optional[str]): A marca do cartão (atributo oculto).

    **Métodos Estáticos**

    * `check_card_number(cls, values) -> str`: Valida e determina a marca do cartão a partir do número.
    * `check_valid_date(cls, value: str) -> str`: Valida a data de expiração do cartão.
    * `check_cvv(cls, value: int) -> int | None`: Valida o código CVV do cartão.
    * `check_holder(cls, value: str) -> str`: Valida o nome do titular do cartão.

    **Configurações**

    * `Config.orm_mode`: Define o modo ORM para serialização.
    """

    holder: str
    number: str
    exp_date: str
    cvv: Optional[int] = None
    brand: Optional[Annotated[str, Field(validate_default=True, hidden=True)]] = None

    @root_validator(pre=True)
    @classmethod
    def check_card_number(cls, values) -> str:
        """
        Valida o número do cartão e determina a marca do cartão.

        Args:
            values (dict): Dicionário contendo os valores do esquema.

        Returns:
            str: O número de cartão validado e com a marca determinada.

        Raises:
            ValueError: Se o número do cartão for inválido.
        """
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
        """
        Valida a data de expiração do cartão.

        Args:
            value (str): A data de expiração do cartão no formato "mm/aaaa".

        Returns:
            str: A data de expiração validada.
        """
        return datetime_validator(value)

    @validator("cvv", pre=True, always=True)
    @classmethod
    def check_cvv(cls, value: int) -> int | None:
        """
        Valida o código CVV do cartão.

        Args:
            value (int): O código CVV do cartão.

        Returns:
            int | None: O código CVV validado ou None se não fornecido.

        Raises:
            ValueError: Se o código CVV for inválido.
        """
        if not value:
            return None

        if isinstance(value, int) and 3 <= len(str(value)) <= 4:
            return value
        raise ValueError("Invalid cvv")

    @validator("holder", pre=True, always=True)
    @classmethod
    def check_holder(cls, value: str) -> str:
        """
        Valida o nome do titular do cartão.

        Args:
            value (str): O nome do titular do cartão.

        Returns:
            str: O nome do titular validado.

        Raises:
            ValueError: Se o nome do titular for muito curto.
        """
        if isinstance(value, str) and len(value) > 2:
            return value
        raise ValueError("Invalid holder, very short statement")

    class Config:
        orm_mode = True