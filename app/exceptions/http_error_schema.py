"""
## Modulo de Serialização de Erros HTTP
"""
from pydantic import BaseModel


class HTTPError(BaseModel):
    """
    Classe HTTPError

    Esta classe representa uma exceção personalizada para erros HTTP. Ela herda da classe BaseModel
    do módulo pydantic e inclui um atributo 'detail' para armazenar informações detalhadas sobre o erro.

    Atributos:
        detail (str): Uma mensagem detalhada que descreve o erro HTTP.

    Configuração:
        A classe HTTPError também possui uma classe interna chamada 'Config', que define
        configurações adicionais para esta classe, como um exemplo de objeto 'schema_extra' para
        fins de documentação.

    Exemplo:
        Um exemplo de uso desta classe seria:

        >>> try:
        ...     # Alguma operação que pode levantar um erro HTTP
        ...     raise HTTPError(detail="HTTPException raised.")
        ... except HTTPError as e:
        ...     print(e.detail)
        ...
        HTTPException raised.

    """

    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "HTTPException raised."},
        }
