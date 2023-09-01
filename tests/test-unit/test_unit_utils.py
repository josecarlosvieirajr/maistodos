from datetime import datetime

import pytest

from app.utils import datetime_validator, hashable


def test_hashable():
    original_text = "senha123"
    hashed_value = hashable(original_text)
    assert isinstance(hashed_value, str)
    assert len(hashed_value) == 64


def test_datetime_validator_with_correct_value():
    input_date = "08/2024"
    formatted_date = datetime_validator(input_date)
    assert isinstance(formatted_date, str)
    assert formatted_date == "2024-08-31"


def test_datetime_validator_with_current_month_and_year():
    now = datetime.now()
    input_date = now.strftime("%m/%Y")
    formatted_date = datetime_validator(input_date)
    assert isinstance(formatted_date, str)


def test_datetime_validator_with_previous_year():
    now = datetime.now()
    input_date = now.strftime("%m/%Y")
    previous_year = now.year - 1
    input_date = input_date.replace(str(now.year), str(previous_year))

    with pytest.raises(ValueError):
        datetime_validator(input_date)


def test_datetime_validator_with_invalid_value():
    input_date = "123/4567"
    with pytest.raises(ValueError):
        datetime_validator(input_date)


def test_datetime_validator_with_numbers_only():
    input_date = "123456"
    with pytest.raises(ValueError):
        datetime_validator(input_date)
