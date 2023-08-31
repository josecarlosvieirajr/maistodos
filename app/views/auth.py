"""
## Módulo com as Views da Autenticação
Este módulo contém as rotas relacionadas à autenticação de usuários na aplicação.
"""

import logging
from datetime import timedelta

from fastapi import APIRouter

from app.auth import Auth, Token, create_access_token
from app.config import settings

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/", response_model=Token)
async def auth(data: Auth):
    """
    Rota de autenticação.

    Esta rota permite a autenticação do usuário e geração de um token de acesso.

    **Parâmetros do Request**

    * `data` (Auth): Dados de autenticação contendo o nome de usuário e a senha.

    **Resposta**

    Retorna um objeto Token que inclui o token de acesso e o tipo de token.

    **Exemplo de Uso**

    ```python
    data = {"username": "usuario", "password": "senha"}
    response = await client.post("/auth/", json=data)
    auth_token = response.json()["access_token"]
    ```

    Args:
        data (Auth): Dados de autenticação.

    Returns:
        value (Token): Token de acesso gerado.
    """
    access_token_expires = timedelta(minutes=settings.token_expire)
    access_token = create_access_token(
        data={"sub": data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
