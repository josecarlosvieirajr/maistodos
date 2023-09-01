import random
import string

import pytest

from app.db.schema import CreditCardSchemaUpdate


class TestCreditCardSchemaUpdate:
    def test_valid_holder_name_with_more_than_2_characters(self):
        holder_name = "John Doe"
        credit_card = CreditCardSchemaUpdate(holder=holder_name)

        assert credit_card.holder == holder_name

    def test_valid_holder_name_with_more_100_characters(self):
        holder_name = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=101)
        )
        with pytest.raises(ValueError):
            CreditCardSchemaUpdate(holder=holder_name)

    def test_valid_holder_name_with_exactly_3_characters(self):
        holder_name = "JDS"
        credit_card = CreditCardSchemaUpdate(holder=holder_name)

        assert credit_card.holder == holder_name

    def test_valid_holder_name_with_exactly_2_characters(self):
        holder_name = "JD"

        with pytest.raises(ValueError):
            CreditCardSchemaUpdate(holder=holder_name)

    def test_holder_name_with_exactly_1_character(self):
        holder_name = "A"

        with pytest.raises(ValueError):
            CreditCardSchemaUpdate(holder=holder_name)

    def test_holder_name_with_none_value(self):
        holder_name = ""

        with pytest.raises(ValueError):
            CreditCardSchemaUpdate(holder=holder_name)

    def test_holder_name_with_more_than_2_characters_and_numbers(self):
        holder_name = "John123"
        credit_card = CreditCardSchemaUpdate(holder=holder_name)

        assert credit_card.holder == holder_name

    def test_holder_name_with_more_than_2_characters_and_special_characters_and_numbers(
        self,
    ):
        holder_name = "John!123"
        credit_card = CreditCardSchemaUpdate(holder=holder_name)

        assert credit_card.holder == holder_name
