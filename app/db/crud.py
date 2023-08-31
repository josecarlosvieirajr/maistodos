"""
Módulo de CRUD genérico para operações de banco de dados.

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

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLModel model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, session: Session, id: int) -> Optional[ModelType]:
        statement = select(self.model).where(self.model.id == id)
        resp = session.exec(statement)
        return resp.one()

    def get_multi(
        self, session: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        statement = select(self.model).offset(skip).limit(limit)
        resp = session.exec(statement)
        return resp.all()

    def create(self, session: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        session.add(db_obj)

        session.commit()
        session.refresh(db_obj)

        return db_obj

    def update(
        self,
        session: Session,
        *,
        obj_in: Union[CreateSchemaType, Dict[str, Any]],
    ) -> ModelType:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = jsonable_encoder(obj_in)
        statement = select(self.model).where(self.model.id == update_data["uuid"])
        results = session.exec(statement)

        db_obj = results.one()
        db_obj.dict().update(update_data)

        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    def remove(self, session: Session, *, id: int) -> ModelType:
        statement = select(self.model).where(self.model.id == id)
        results = session.exec(statement)
        db_obj = results.one()

        session.delete(db_obj)
        session.commit()
        return db_obj
