from datetime import timedelta
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from app import create_app
from app.auth import create_access_token
from app.db.model import get_session


@pytest.fixture
def app():
    return create_app()


@pytest.fixture(scope="function")
def create_token() -> str:
    return create_access_token({"sub": "test"}, timedelta(minutes=5))


@pytest.fixture(scope="function")
def header(create_token) -> dict:
    return {"token": create_token}


@pytest.fixture(scope="function")
def url_v1() -> str:
    return "/api/v1"


@pytest.fixture(name="session")
def session():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="function")
def client(app, session: Session) -> Generator:
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
