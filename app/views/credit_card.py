"""
## Módulo com as Visualizações (Views) de Cartão de Crédito
Este módulo contém as rotas relacionadas à manipulação de informações de cartão de crédito.

As rotas disponíveis incluem:
- Listagem de todos os cartões de crédito
- Detalhes de um cartão de crédito por ID
- Criação de um novo cartão de crédito
- Atualização de informações de um cartão de crédito
- Exclusão de um cartão de crédito por ID
"""
import logging
from typing import List

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from app.auth import check_token
from app.db.model import CreditCard, get_session
from app.db.repository import credit_card_repository
from app.db.schema import CreditCardSchema, CreditCardSchemaUpdate, HTTPError

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/", response_model=List[CreditCard])
async def list_all_credit_card(
    *,
    session: Session = Depends(get_session),
    skip: int = Query(default=0, lte=100),
    limit: int = Query(default=100, lte=100),
    username: str = Depends(check_token)
):
    """
    Lista todos os cartões de crédito disponíveis.

    Esta função retorna uma lista de cartões de crédito com base nos parâmetros especificados.

    Parâmetros:
        session (Session): Uma sessão de banco de dados obtida usando `get_session` (opcional).
        skip (int): O número de cartões de crédito a serem ignorados (padrão é 0, no máximo 100).
        limit (int): O número máximo de cartões de crédito a serem retornados (padrão é 100, no máximo 100).
        username (str): O nome de usuário obtido a partir do token de autenticação (opcional).

    Retorna:
        List[CreditCard]: Uma lista de objetos `CreditCard` representando os cartões de crédito.

    Exemplo:
        >>> username = "john_doe"
        >>> credit_cards = await list_all_credit_card(username=username)

    Exceções:
        HTTPException(400, "Limit deve ser no máximo 100"): Se o parâmetro `limit` for superior a 100.
        HTTPException(400, "Skip deve ser no máximo 100"): Se o parâmetro `skip` for superior a 100.

    """
    credit_card_repository.set_username(username)
    resp = credit_card_repository.get_multi(session, skip=skip, limit=limit)
    return resp


@router.get(
    "/{id}",
    responses={
        200: {"model": CreditCard},
        404: {"model": HTTPError, "description": "Credit card not found"},
    },
)
async def get_credit_card_for_key(
    id: int,
    *,
    session: Session = Depends(get_session),
    username: str = Depends(check_token)
):
    """
    Obtém informações de um cartão de crédito com base em seu ID.

    Esta função recebe um ID como parâmetro e retorna as informações do cartão de crédito correspondente,
    se existir. Caso contrário, lança uma exceção HTTP 404 indicando que o cartão de crédito não foi encontrado.

    Parâmetros:
        id (int): O ID do cartão de crédito que deseja ser consultado.
        session (Session): Uma sessão de banco de dados obtida usando `get_session` (opcional).
        username (str): O nome de usuário obtido a partir do token de autenticação (opcional).

    Retorna:
        CreditCard: Um objeto `CreditCard` com as informações do cartão de crédito.

    Exemplo:
        >>> card_id = 123
        >>> username = "john_doe"
        >>> credit_card = await get_credit_card_for_key(id=card_id, username=username)

    Exceções:
        HTTPException(404, "Cartão de crédito não encontrado"): Se o cartão de crédito com o ID especificado não for encontrado.

    """
    credit_card_repository.set_username(username)
    resp = credit_card_repository.get(session, id=id)
    return resp


@router.post(
    "/",
    responses={
        200: {"model": CreditCard},
        409: {
            "model": HTTPError,
            "description": "Conflict, this card number already exists",
        },
    },
)
async def create_credit(
    *,
    session: Session = Depends(get_session),
    data: CreditCardSchema,
    username: str = Depends(check_token)
):
    """
    Criação de um novo cartão de crédito.

    Esta rota permite criar um novo cartão de crédito com as informações fornecidas.

    Parâmetros:
        session (Session): Uma sessão do banco de dados obtida usando `get_session`.
        data (CreditCardSchema): Os dados do cartão de crédito a serem criados.
        username (str): O nome de usuário obtido a partir do token de autenticação.

    Retorna:
        CreditCard: Um objeto representando o cartão de crédito recém-criado.

    Exceções:
        HTTPException(409, "Conflito, este número de cartão já existe"):
            Se o número do cartão já estiver em uso.

    Exemplo:
        >>> data = CreditCardSchema(
        ...     card_number="1234-5678-9012-3456",
        ...     expiration_date="12/24",
        ...     owner_name="John Doe",
        ...     balance=1000.0,
        ... )
        >>> username = "john_doe"
        >>> credit_card = await create_credit(session=session, data=data, username=username)

    """
    credit_card_repository.set_username(username)
    resp = credit_card_repository.create(session, obj_in=data)
    return resp


@router.put(
    "/{id}",
    responses={
        200: {"model": CreditCard},
        404: {"model": HTTPError, "description": "Credit card not found"},
    },
)
async def update_credit_card_for_key(
    id: int,
    *,
    data: CreditCardSchemaUpdate,
    session: Session = Depends(get_session),
    username: str = Depends(check_token)
):
    """
    Atualização de informações de um cartão de crédito.

    Esta rota permite atualizar as informações de um cartão de crédito específico pelo seu ID.

    !!! note "Nota"
        Como a atualização é feita em um cartão de crédito já existente, o número do cartão não pode ser alterado.

        Nesse modelo, permitimos apenas a atualização do nome do titular do cartão, para efeito de demonstração.

    Parâmetros:
        id (int): O ID do cartão de crédito a ser atualizado.
        data (CreditCardSchemaUpdate): Os dados atualizados do cartão de crédito.
        session (Session): Uma sessão do banco de dados obtida usando `get_session`.
        username (str): O nome de usuário obtido a partir do token de autenticação.

    Retorna:
        CreditCard: Um objeto representando o cartão de crédito após a atualização.

    Exceções:
        HTTPException(404, "Cartão de crédito não encontrado"):
            Se o cartão de crédito com o ID especificado não for encontrado.

    Exemplo:
        >>> card_id = 123
        >>> updated_data = CreditCardSchemaUpdate(
        ...     expiration_date="12/25",
        ...     owner_name="John Doe Jr.",
        ... )
        >>> username = "john_doe"
        >>> updated_credit_card = await update_credit_card_for_key(
        ...     id=card_id, data=updated_data, session=session, username=username
        ... )

    """
    credit_card_repository.set_username(username)
    resp = credit_card_repository.update(session, id=id, obj_in=data)
    return resp


@router.delete(
    "/{id}",
    responses={
        200: {"model": CreditCard},
        404: {"model": HTTPError, "description": "Credit card not found"},
    },
)
async def delete_credit_card_for_key(
    id: int,
    *,
    session: Session = Depends(get_session),
    username: str = Depends(check_token)
):
    """
    Exclusão de um cartão de crédito.

    Esta rota permite excluir um cartão de crédito específico pelo seu ID.


    Parâmetros:
        id (int): O ID do cartão de crédito a ser excluído.
        session (Session): Uma sessão do banco de dados obtida usando `get_session`.
        username (str): O nome de usuário obtido a partir do token de autenticação.

    Retorna:
        CreditCard: Um objeto representando o cartão de crédito excluído.

    Exceções:
        HTTPException(404, "Cartão de crédito não encontrado"):
            Se o cartão de crédito com o ID especificado não for encontrado.

    Exemplo:
        >>> card_id = 123
        >>> username = "john_doe"
        >>> deleted_credit_card = await delete_credit_card_for_key(
        ...     id=card_id, session=session, username=username
        ... )

    """
    credit_card_repository.set_username(username)
    resp = credit_card_repository.remove(session, id=id)
    return resp
