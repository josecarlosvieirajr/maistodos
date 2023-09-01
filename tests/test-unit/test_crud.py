from typing import Any

import pytest

from app.db.crud import CRUDBase
from tests.mocks.model import TesteBase


class TestCRUDBase:
    def __init__(self):
        self.crud_base = CRUDBase(TesteBase)

    def test_get_valid_id_with_empty_db(self, session):
        result = self.crud_base.get(session, 1)

        assert result is None

    def test_get_valid_id_with_db_fill(self, session):
        expected = self.crud_base.create(session, obj_in={"name": "Teste"})
        result: Any = self.crud_base.get(session, 1)

        assert result.id == expected.id
        assert result.name == "Teste"

    def test_get_multi_valid_skip_limit(self, session):
        expected = 2
        self.crud_base.create(session, obj_in={"name": "Teste1"})
        self.crud_base.create(session, obj_in={"name": "Teste2"})
        self.crud_base.create(session, obj_in={"name": "Teste3"})
        result = self.crud_base.get_multi(session, skip=0, limit=expected)

        assert len(result) == expected

    def test_update_valid_id_input(self, session):
        expected = "TESTE2"
        self.crud_base.create(session, obj_in={"name": "Teste1"})
        res = self.crud_base.update(session, id=1, obj_in={"name": expected})

        assert res.name == expected

    def test_update_valid_id_input_in_empty_value(self, session):
        with pytest.raises(ValueError):
            self.crud_base.update(session, id=15, obj_in={"name": "Any"})

    def test_remove_valid_id(self, session):
        expected = "Teste1"
        self.crud_base.create(session, obj_in={"name": expected})
        res = self.crud_base.remove(session, id=1)

        assert res.name == expected

    def test_get_invalid_id(self, session):
        result = self.crud_base.get(session, 132)

        assert result is None

    def test_get_multi_invalid_skip_limit(self, session):
        result = self.crud_base.get_multi(session, skip=0, limit=-1)
        assert result is None
