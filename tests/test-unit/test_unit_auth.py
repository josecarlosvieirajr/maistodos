import pytest
from fastapi import HTTPException

from app.auth import check_token, create_access_token
from tests.mocks.auth import generate_expire_token


def test_create_access_token():
    token = create_access_token(data={"sub": "testuser"})
    assert isinstance(token, str)
    assert len(token.split(".")) == 3


def test_create_access_token_without_data():
    token = create_access_token(data={})
    assert isinstance(token, str)
    assert len(token.split(".")) == 3


def test_create_access_token_with_data_but_username_empty():
    token = create_access_token(data={"sub": None})
    assert isinstance(token, str)
    assert len(token.split(".")) == 3


def test_create_access_token_with_data_but_username_not_string():
    token = create_access_token(data={"sub": 123})
    assert isinstance(token, str)
    assert len(token.split(".")) == 3


def test_check_token_with_sub_default():
    expected = "testuser"
    token = create_access_token(data={"sub": expected})
    assert check_token(token=token) == expected


def test_check_token_without_sub_data():
    token = create_access_token(data={})
    with pytest.raises(HTTPException):
        check_token(token=token)


def test_check_token_with_data_but_username_empty():
    token = create_access_token(data={"sub": None})
    with pytest.raises(HTTPException):
        check_token(token=token)


def test_check_token_with_data_but_username_not_string():
    token = create_access_token(data={"sub": 123})
    with pytest.raises(HTTPException):
        check_token(token=token)


def test_check_token_with_expired_token():
    token = generate_expire_token()
    with pytest.raises(HTTPException):
        check_token(token=token)
