"""
## Modulo de Models e Banco de Dados.

"""

import logging
from datetime import datetime
from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine

from app.config import settings

logger = logging.getLogger(__name__)


class Base(SQLModel):
    """
    Classe base para modelos comuns.

    Essa classe define campos comuns para modelos, como ID, data de criação e data de atualização.

    **Atributos**

    * `id` (Optional[int]): O ID da instância.
    * `created_at` (datetime): A data e hora de criação da instância.
    * `updated_at` (datetime): A data e hora da última atualização da instância.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow(), index=True)
    updated_at: datetime = Field(default=datetime.utcnow(), index=True)


class CreditCardBase(SQLModel):
    """
    Classe base para informações de cartão de crédito.

    Essa classe define campos comuns para informações de cartão de crédito, como titular, número, data de expiração e CVV.

    **Atributos**

    * `holder` (str): O nome do titular do cartão.
    * `number` (str): O número único do cartão.
    * `exp_date` (str): A data de expiração do cartão.
    * `cvv` (Optional[int]): O código CVV do cartão (opcional).
    """

    holder: str = Field(index=True)
    number: str = Field(unique=True)
    exp_date: str
    cvv: Optional[int] = None


class CreditCard(Base, CreditCardBase, table=True):
    """
    Classe que representa informações de um cartão de crédito.

    Essa classe herda os campos da classe Base e CreditCardBase para definir um modelo completo
    de informações de cartão de crédito, incluindo a marca do cartão.

    **Atributos**

    * `brand` (str): A marca do cartão.
    """

    brand: str = Field(index=True)


connect_args = {"check_same_thread": False}
engine = create_engine(settings.database_url, echo=True, connect_args=connect_args)


def get_session():
    """
    Retorna uma sessão do banco de dados.

    Essa função cria e retorna uma sessão do banco de dados usando o motor de banco de dados configurado.

    Yields:
        value (Session): Uma sessão do banco de dados.
    """
    with Session(engine) as session:
        yield session
