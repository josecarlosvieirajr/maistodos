from app.config import settings
from app.db.model import get_session


def test_get_session():
    session = next(get_session())
    assert session.is_active
    conn = session.connection()
    assert conn.engine.name == "sqlite"
    assert str(conn.engine.url) == settings.database_url


def test_session_pytest_generate(session):
    assert session.is_active
    conn = session.connection()
    assert conn.engine.name == "sqlite"
    assert str(conn.engine.url) == "sqlite://"
