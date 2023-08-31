from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.fixture(scope="function")
def client(app) -> Generator:
    with TestClient(app) as c:
        yield c
