from typing import Any

import pytest

from app.db.schema import CreditCardSchema

from tests.mocks.credit_card import (  # isort:skip
    VALID_MASTER_CREDIT_CARD_NUMBER,  # isort:skip
    VALID_VISA_CREDIT_CARD_NUMBER,  # isort:skip
)  # isort:skip


class TestCreditCardSchema:
    def test_valid_input_data(self):
        input_data = {
            "holder": "John Doe",
            "number": VALID_VISA_CREDIT_CARD_NUMBER,
            "exp_date": "12/2023",
            "cvv": 123,
        }

        result = CreditCardSchema(**input_data)

        assert result.holder == "John Doe"
        assert result.number != VALID_VISA_CREDIT_CARD_NUMBER
        assert isinstance(result.number, str)
        assert len(result.number) == 64
        assert result.exp_date == "2023-12-31"
        assert result.cvv == 123
        assert result.brand == "visa"

    def test_optional_cvv_field_with_visa(self):
        input_data: Any = {
            "holder": "John Doe",
            "number": VALID_VISA_CREDIT_CARD_NUMBER,
            "exp_date": "12/2023",
        }

        result = CreditCardSchema(**input_data)

        assert result.holder == "John Doe"
        assert result.number != VALID_VISA_CREDIT_CARD_NUMBER
        assert isinstance(result.number, str)
        assert len(result.number) == 64
        assert result.exp_date == "2023-12-31"
        assert result.cvv is None
        assert result.brand == "visa"

    def test_optional_cvv_field_with_master(self):
        input_data: Any = {
            "holder": "John Doe",
            "number": VALID_MASTER_CREDIT_CARD_NUMBER,
            "exp_date": "12/2023",
        }

        result = CreditCardSchema(**input_data)

        assert result.holder == "John Doe"
        assert result.number != VALID_MASTER_CREDIT_CARD_NUMBER
        assert isinstance(result.number, str)
        assert len(result.number) == 64
        assert result.exp_date == "2023-12-31"
        assert result.cvv is None
        assert result.brand == "master"

    def test_valid_input_data_with_hidden_brand_field(self):
        input_data: Any = {
            "holder": "John Doe",
            "number": VALID_VISA_CREDIT_CARD_NUMBER,
            "exp_date": "12/2023",
            "brand": "TESTE",
        }

        result = CreditCardSchema(**input_data)

        assert result.holder == "John Doe"
        assert result.number != VALID_VISA_CREDIT_CARD_NUMBER
        assert isinstance(result.number, str)
        assert len(result.number) == 64
        assert result.exp_date == "2023-12-31"
        assert result.cvv is None
        assert result.brand == "visa"

    def test_invalid_card_number(self):
        input_data = {
            "holder": "John Doe",
            "number": "1234567890123456",
            "exp_date": "12/2023",
            "cvv": 123,
        }

        with pytest.raises(ValueError):
            CreditCardSchema(**input_data)

    def test_valid_card_number_with_special_characters(self):
        n = 4
        chunks = [
            VALID_VISA_CREDIT_CARD_NUMBER[i : i + n]  # noqa: E203
            for i in range(0, len(VALID_VISA_CREDIT_CARD_NUMBER), n)
        ]
        valid_card_with_special_char = "-".join(chunks)
        input_data = {
            "holder": "John Doe",
            "number": valid_card_with_special_char,
            "exp_date": "12/2023",
            "cvv": 123,
        }

        result = CreditCardSchema(**input_data)

        assert result.holder == "John Doe"
        assert result.number != VALID_VISA_CREDIT_CARD_NUMBER
        assert isinstance(result.number, str)
        assert len(result.number) == 64
        assert result.exp_date == "2023-12-31"
        assert result.cvv == 123
        assert result.brand == "visa"

    def test_invalid_card_number_with_special_characters(self):
        input_data = {
            "holder": "John Doe",
            "number": "1111-1111-1111-1111",
            "exp_date": "12/2023",
            "cvv": 123,
        }

        with pytest.raises(ValueError):
            CreditCardSchema(**input_data)

    def test_invalid_card_number_with_letters(self):
        input_data = {
            "holder": "John Doe",
            "number": "411111111111111a",
            "exp_date": "12/2023",
            "cvv": 123,
        }

        with pytest.raises(ValueError):
            CreditCardSchema(**input_data)

    def test_invalid_card_number_with_less_than_12_digits(self):
        input_data = {
            "holder": "John Doe",
            "number": "41111111111",
            "exp_date": "12/2023",
            "cvv": 123,
        }

        with pytest.raises(ValueError):
            CreditCardSchema(**input_data)

    def test_invalid_card_number_with_more_than_19_digits(self):
        input_data = {
            "holder": "John Doe",
            "number": "41111111111111111111",
            "exp_date": "12/2023",
            "cvv": 123,
        }

        with pytest.raises(ValueError):
            CreditCardSchema(**input_data)
