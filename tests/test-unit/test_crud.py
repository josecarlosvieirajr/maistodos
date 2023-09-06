from typing import Any

import pytest

from app.db.crud import CRUDBase
from app.db.model import Base
from app.exceptions.crud_error import CRUDDeleteError, CRUDSelectError, CRUDUpdateError


class BaseUnitTestModel(Base, table=True):
    holder: str


crud_base = CRUDBase(BaseUnitTestModel)


def test_get_valid_id_with_empty_db(session):
    with pytest.raises(CRUDSelectError):
        crud_base.get(session, 1)


def test_get_valid_id_with_db_fill(session):
    expected = crud_base.create(session, obj_in={"holder": "Teste"})
    result: Any = crud_base.get(session, 1)

    assert result.id == expected.id
    assert result.holder == "Teste"


def test_get_multi_valid_skip_limit(session):
    expected = 2
    crud_base.create(session, obj_in={"holder": "Teste1"})
    crud_base.create(session, obj_in={"holder": "Teste2"})
    crud_base.create(session, obj_in={"holder": "Teste3"})
    result = crud_base.get_multi(session, skip=0, limit=expected)

    assert len(result) == expected


def test_update_valid_id_input(session):
    expected = "TESTE2"
    crud_base.create(session, obj_in={"holder": "Teste1"})
    res = crud_base.update(session, id=1, obj_in={"holder": expected})

    assert res.holder == expected


def test_remove_valid_id(session):
    expected = "Teste1"
    crud_base.create(session, obj_in={"holder": expected})
    res = crud_base.remove(session, id=1)

    assert res.holder == expected


def test_get_invalid_id(session):
    with pytest.raises(CRUDSelectError):
        crud_base.get(session, 132)


def test_get_multi_invalid_skip_limit(session):
    result = crud_base.get_multi(session, skip=0, limit=-1)
    assert isinstance(result, list)
    assert len(result) == 0


def test_remove_not_exists_item(session):
    with pytest.raises(CRUDDeleteError):
        crud_base.remove(session, id=1)


def test_update_valid_id_input_in_empty_value(session):
    expect_id = 15
    with pytest.raises(CRUDUpdateError):
        crud_base.update(session, id=expect_id, obj_in={"holder": "Any"})
