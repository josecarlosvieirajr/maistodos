from app.db.schema import CreditCardSchema

VALID_VISA_CREDIT_CARD_NUMBER = "4539578763621486"
VALID_MASTER_CREDIT_CARD_NUMBER = "5186001700009726"
INVALID_CREDIT_CARD_NUMBER = "1111111111111111"


valid_visa_credit_card = CreditCardSchema(
    holder="Test User 1",
    number=VALID_VISA_CREDIT_CARD_NUMBER,
    exp_date="01/2029",
    cvv=123,
)

valid_master_credit_card = CreditCardSchema(
    holder="Test User 2",
    number=VALID_MASTER_CREDIT_CARD_NUMBER,
    exp_date="01/2029",
    cvv=123,
)

valid_visa_credit_card_json = {
    "holder": "Test User 1",
    "number": VALID_VISA_CREDIT_CARD_NUMBER,
    "exp_date": "01/2029",
    "cvv": 123,
}

valid_master_credit_card_json = {
    "holder": "Test User 1",
    "number": VALID_MASTER_CREDIT_CARD_NUMBER,
    "exp_date": "01/2029",
    "cvv": 123,
}

invalid_credit_card_json = {
    "holder": "Test User 3",
    "number": INVALID_CREDIT_CARD_NUMBER,
    "exp_date": "01/2029",
    "cvv": 123,
}

valid_master_credit_card_with_cvv_none_json = {
    "holder": "Test User 2",
    "number": VALID_MASTER_CREDIT_CARD_NUMBER,
    "exp_date": "01/2029",
    "cvv": None,
}

valid_master_credit_card_with_invalid_cvv_json = {
    "holder": "Test User 2",
    "number": VALID_MASTER_CREDIT_CARD_NUMBER,
    "exp_date": "01/2029",
    "cvv": "abc",
}

valid_master_credit_card_with_cvv_to_4_digits_json = {
    "holder": "Test User 2",
    "number": VALID_MASTER_CREDIT_CARD_NUMBER,
    "exp_date": "01/2029",
    "cvv": 1234,
}

valid_master_credit_card_with_invalid_holder_json = {
    "holder": "F",
    "number": VALID_MASTER_CREDIT_CARD_NUMBER,
    "exp_date": "01/2029",
    "cvv": 123,
}

valid_master_credit_card_with_invalid_date_json = {
    "holder": "F",
    "number": VALID_MASTER_CREDIT_CARD_NUMBER,
    "exp_date": "01/2022",
    "cvv": 123,
}
