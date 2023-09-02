"""
## Modulo que cria a ação dos Verbos HTTP.
Módulo que define ações relacionadas aos Verbos HTTP para manipulação de cartões de crédito.
Cria um especificação do modulo generico de CRUD.
"""

from typing import Any, Dict

from sqlmodel import Session

from app.db.crud import CRUDBase
from app.db.model import CreditCard
from app.db.schema import CreditCardSchema, CreditCardSchemaUpdate


class CartRepository(CRUDBase[CreditCard, CreditCardSchema, CreditCardSchemaUpdate]):
    """
    Classe responsável por operações CRUD em relação aos cartões de crédito.

    Essa classe herda os métodos CRUD da classe CRUDBase para interagir com os dados dos cartões de crédito.

    **Métodos**

    * `get(session: Session, id: int) -> Optional[CreditCard]`: Retorna um cartão de crédito pelo ID.
    * `get_multi(session: Session, *, skip: int = 0, limit: int = 100) -> List[CreditCard]`: Retorna uma lista paginada de cartões de crédito.
    * `create(session: Session, *, obj_in: CreditCardSchema) -> CreditCard`: Cria um novo cartão de crédito.
    * `update(session: Session, *, id: int, obj_in: CreditCardSchemaUpdate) -> CreditCard`: Atualiza um cartão de crédito existente.
    * `remove(session: Session, *, id: int) -> CreditCard`: Remove um cartão de crédito pelo ID.
    """

    def update(
        self,
        session: Session,
        *,
        id: int,
        obj_in: CreditCardSchemaUpdate | Dict[str, Any]
    ) -> CreditCard:
        db_obj = self.convert_any_to_dict(obj_in)
        return super().update(session, id=id, obj_in={"holder": db_obj["holder"]})


credit_card_repository = CartRepository(CreditCard)
