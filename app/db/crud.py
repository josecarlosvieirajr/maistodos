"""
## Módulo de CRUD genérico para operações de banco de dados.

Attributes:
    GET: Método de leitura de dados.
    GET_MULTI: Método de leitura de vários dados.
    CREATE: Método de criação de dados.
    UPDATE: Método de atualização de dados.
    REMOVE: Método de remoção de dados.

"""


from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlmodel import Session, select

from app.db.model import Base
from app.exceptions.crud_error import CRUDUpdateError

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    Classe base para operações CRUD (Create, Read, Update, Delete) em um modelo.

    Essa classe fornece métodos padrão para realizar operações CRUD em um modelo,
    incluindo busca por ID, busca múltipla com paginação, criação, atualização e exclusão.

    **Parâmetros**

    * `model`: Uma classe modelo SQLModel.
    * `schema`: Uma classe modelo Pydantic (schema).

    **Atributos**

    * `model`: A classe modelo associada à instância CRUD.

    **Métodos**

    * `get(session: Session, id: int) -> Optional[ModelType]`: Retorna uma instância do modelo com o ID correspondente.
    * `get_multi(session: Session, *, skip: int = 0, limit: int = 100) -> List[ModelType]`: Retorna uma lista paginada de instâncias do modelo.
    * `create(session: Session, *, obj_in: CreateSchemaType) -> ModelType`: Cria uma nova instância do modelo com os dados fornecidos.
    * `update(session: Session, *, id: int, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType`: Atualiza
    uma instância do modelo com os dados fornecidos.
    * `remove(session: Session, *, id: int) -> ModelType`: Remove uma instância do modelo com o ID correspondente.
    """

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def _commit_and_refresh(self, session: Session, db_obj: ModelType) -> ModelType:
        session.commit()
        session.refresh(db_obj)
        return db_obj

    def convert_any_to_dict(
        self, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> Dict[str, Any]:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = jsonable_encoder(obj_in)
        return update_data

    def get(self, session: Session, id: int) -> Optional[ModelType]:
        """
        Retorna uma instância do modelo com o ID correspondente.

        Args:
            session (Session): A sessão do banco de dados.
            id (int): O ID da instância a ser buscada.

        Returns:
            value (Optional[ModelType]): A instância do modelo, se encontrada; caso contrário, None.
        """
        return session.get(self.model, id)

    def get_multi(
        self, session: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        """
        Retorna uma lista paginada de instâncias do modelo.

        Args:
            session (Session): A sessão do banco de dados.
            skip (int, opcional): O número de registros a serem ignorados.
            limit (int, opcional): O número máximo de registros a serem retornados.

        Returns:
            value (List[ModelType]): Uma lista de instâncias do modelo.
        """
        statement = select(self.model).offset(skip).limit(limit)
        results = session.exec(statement)
        return results.all()

    def create(self, session: Session, *, obj_in: CreateSchemaType) -> ModelType:
        """
        Cria uma nova instância do modelo com os dados fornecidos.

        Args:
            session (Session): A sessão do banco de dados.
            obj_in (CreateSchemaType): Os dados para criar a nova instância.

        Returns:
            value (ModelType): A instância do modelo recém-criada.
        """
        db_obj = self.model.parse_obj(obj_in)
        session.add(db_obj)
        return self._commit_and_refresh(session, db_obj)

    def update(
        self,
        session: Session,
        *,
        id: int,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> ModelType:
        """
        Atualiza uma instância do modelo com os dados fornecidos.

        Args:
            session (Session): A sessão do banco de dados.
            id (int): O ID da instância a ser atualizada.
            obj_in (Union[UpdateSchemaType, Dict[str, Any]]): Os dados para atualizar a instância.

        Returns:
            value (ModelType): A instância do modelo atualizada.
        """
        result = session.get(self.model, id)

        if not result:
            raise CRUDUpdateError(obj_id=id)

        result_data = self.convert_any_to_dict(obj_in)

        for key, value in result_data.items():
            setattr(result, key, value)

        session.add(result)
        return self._commit_and_refresh(session, result)

    def remove(self, session: Session, *, id: int) -> ModelType:
        """
        Remove uma instância do modelo com o ID correspondente.

        Args:
            session (Session): A sessão do banco de dados.
            id (int): O ID da instância a ser removida.

        Returns:
            value (ModelType): A instância do modelo removida.
        """
        result = session.get(self.model, id)

        if not result:
            raise ValueError("ID does not exist")

        session.delete(result)
        session.commit()
        return result
