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
    """
    Lista todos os cartões de crédito.

    Esta rota permite listar todos os cartões de crédito presentes no sistema.

    **Parâmetros do Request**

    * `session` (Session): Sessão do banco de dados.
    * `skip` (int): Número de registros para pular (para paginação).
    * `limit` (int): Número máximo de registros a serem retornados (para paginação).
    * `username` (str): Nome de usuário obtido a partir do token de acesso.

    O Parametro `username` é usado apenas pra validar o token,
    em um cenário com uma tabala de user, poderia ser usado para validar a permissão do usuário.

    Returns:
        value (List[CreditCard]): Lista de objetos de cartão de crédito.
    """
    resp = credit_card_repository.get_multi(session, skip=skip, limit=limit)
    return resp


@router.get("/{id}", response_model=CreditCard)
async def get_credit_card_for_key(
    id: int,
    *,
    session: Session = Depends(get_session),
    username: str = Depends(check_token)
):
    """
    Detalhes de um cartão de crédito.

    Esta rota permite obter detalhes de um cartão de crédito específico pelo seu ID.

    **Parâmetros do Request**

    * `id` (int): ID do cartão de crédito.
    * `session` (Session): Sessão do banco de dados.
    * `username` (str): Nome de usuário obtido a partir do token de acesso.

    O Parametro `username` é usado apenas pra validar o token,
    em um cenário com uma tabala de user, poderia ser usado para validar a permissão do usuário.

    Returns:
        value (CreditCard): Objeto de cartão de crédito.
    """
    resp = credit_card_repository.get(session, id=id)
    return resp


@router.post("/", status_code=status.HTTP_200_OK)
async def create_credit(
    *,
    session: Session = Depends(get_session),
    data: CreditCardSchema,
    username: str = Depends(check_token)
):
    """
    Criação de um novo cartão de crédito.

    Esta rota permite criar um novo cartão de crédito com as informações fornecidas.

    **Parâmetros do Request**

    * `session` (Session): Sessão do banco de dados.
    * `data` (CreditCardSchema): Dados do cartão de crédito a ser criado.
    * `username` (str): Nome de usuário obtido a partir do token de acesso.

    O Parametro `username` é usado apenas pra validar o token,
    em um cenário com uma tabala de user, poderia ser usado para validar a permissão do usuário.

    Returns:
        value (CreditCard): Objeto de cartão de crédito criado.

    Raises:
        HTTPException: Se o número do cartão já existir.
    """
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
    """
    Atualização de informações de um cartão de crédito.

    Esta rota permite atualizar as informações de um cartão de crédito específico pelo seu ID.

    !!! note "Nota"
        Como a atualização é feita em um cartão de crédito já existente, o número do cartão não pode ser alterado.

        Nesse modelo, permitimos apenas a atualização do nome do titular do cartão, para efeito de demonstração.

    **Parâmetros do Request**

    * `id` (int): ID do cartão de crédito a ser atualizado.
    * `data` (CreditCardSchemaUpdate): Dados do cartão de crédito a serem atualizados.
    * `session` (Session): Sessão do banco de dados.
    * `username` (str): Nome de usuário obtido a partir do token de acesso.

    O Parametro `username` é usado apenas pra validar o token,
    em um cenário com uma tabala de user, poderia ser usado para validar a permissão do usuário.

    Returns:
        value (CreditCard): Objeto de cartão de crédito atualizado.
    """
    resp = credit_card_repository.update(session, id=id, obj_in=data)
    return resp


@router.delete("/{id}", response_model=CreditCard)
async def delete_credit_card_for_key(
    id: int,
    *,
    session: Session = Depends(get_session),
    username: str = Depends(check_token)
):
    """
    Exclusão de um cartão de crédito.

    Esta rota permite excluir um cartão de crédito específico pelo seu ID.

    **Parâmetros do Request**

    * `id` (int): ID do cartão de crédito a ser excluído.
    * `session` (Session): Sessão do banco de dados.
    * `username` (str): Nome de usuário obtido a partir do token de acesso.

    O Parametro `username` é usado apenas pra validar o token,
    em um cenário com uma tabala de user, poderia ser usado para validar a permissão do usuário.

    Returns:
        value (CreditCard): Objeto de cartão de crédito excluído.
    """

    resp = credit_card_repository.remove(session, id=id)
    return resp
