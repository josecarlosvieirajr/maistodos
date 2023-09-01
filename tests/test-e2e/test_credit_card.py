from unittest.mock import patch

import pytest

from app.db.repository import credit_card_repository
from tests.mocks.auth import INVALID_TOKEN
from tests.mocks.credit_card import (
    invalid_credit_card_json,
    valid_master_credit_card,
    valid_master_credit_card_json,
    valid_master_credit_card_with_cvv_none_json,
    valid_master_credit_card_with_cvv_to_4_digits_json,
    valid_master_credit_card_with_invalid_cvv_json,
    valid_master_credit_card_with_invalid_date_json,
    valid_master_credit_card_with_invalid_holder_json,
    valid_visa_credit_card,
    valid_visa_credit_card_json,
)


def test_create_credit(client, url_v1, header):
    holder = valid_visa_credit_card_json["holder"]
    response = client.post(
        f"{url_v1}/credit-card/", json=valid_visa_credit_card_json, headers=header
    )
    assert response.status_code == 200
    assert response.json()["holder"] == holder


def test_create_credit_with_invalid_card_number(client, url_v1, header):
    response = client.post(
        f"{url_v1}/credit-card/", json=invalid_credit_card_json, headers=header
    )
    assert response.status_code == 422
    assert response.json()["detail"]


def test_create_credit_with_invalid_cvv_number(client, url_v1, header):
    response = client.post(
        f"{url_v1}/credit-card/",
        json=valid_master_credit_card_with_invalid_cvv_json,
        headers=header,
    )
    assert response.status_code == 422
    assert response.json()["detail"]


def test_create_credit_with_valid_cvv_to_4_number(client, url_v1, header):
    holder = valid_master_credit_card_with_cvv_to_4_digits_json["holder"]
    response = client.post(
        f"{url_v1}/credit-card/",
        json=valid_master_credit_card_with_cvv_to_4_digits_json,
        headers=header,
    )
    assert response.status_code == 200
    assert response.json()["holder"] == holder


def test_create_credit_with_invalid_date(client, url_v1, header):
    response = client.post(
        f"{url_v1}/credit-card/",
        json=valid_master_credit_card_with_invalid_date_json,
        headers=header,
    )
    assert response.status_code == 422
    assert response.json()["detail"]


def test_create_credit_with_invalid_holder(client, url_v1, header):
    response = client.post(
        f"{url_v1}/credit-card/",
        json=valid_master_credit_card_with_invalid_holder_json,
        headers=header,
    )
    assert response.status_code == 422
    assert response.json()["detail"]


def test_create_credit_with_cvv_none(client, url_v1, header):
    holder = valid_master_credit_card_with_cvv_none_json["holder"]
    response = client.post(
        f"{url_v1}/credit-card/",
        json=valid_master_credit_card_with_cvv_none_json,
        headers=header,
    )
    assert response.status_code == 200
    assert response.json()["holder"] == holder


def test_registering_same_card_in_bank_twice(client, url_v1, header):
    client.post(
        f"{url_v1}/credit-card/", json=valid_visa_credit_card_json, headers=header
    )
    response = client.post(
        f"{url_v1}/credit-card/", json=valid_visa_credit_card_json, headers=header
    )

    assert response.status_code == 409
    assert response.json()["detail"] == "this card number already exists"


def test_registering_same_holder_in_bank_twice(client, url_v1, header):
    holder_1 = valid_visa_credit_card_json["holder"]
    holder_2 = valid_master_credit_card_json["holder"]
    client.post(
        f"{url_v1}/credit-card/", json=valid_visa_credit_card_json, headers=header
    )
    response = client.post(
        f"{url_v1}/credit-card/", json=valid_master_credit_card_json, headers=header
    )

    assert response.status_code == 200
    assert response.json()["holder"] == holder_1 == holder_2


def test_list_all_credit_card(client, url_v1, header, session):
    credit_card_repository.create(session, obj_in=valid_visa_credit_card)
    credit_card_repository.create(session, obj_in=valid_master_credit_card)

    response = client.get(f"{url_v1}/credit-card/", headers=header)
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_credit_card_for_key(client, url_v1, header, session):
    holder = valid_visa_credit_card.holder
    card = credit_card_repository.create(session, obj_in=valid_visa_credit_card)

    response = client.get(f"{url_v1}/credit-card/{card.id}", headers=header)
    assert response.status_code == 200
    assert response.json()["holder"] == holder


def test_get_credit_card_for_key_with_invalid_token(client, url_v1, session):
    card = credit_card_repository.create(session, obj_in=valid_visa_credit_card)

    response = client.get(
        f"{url_v1}/credit-card/{card.id}", headers={"token": INVALID_TOKEN}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_update_credit_card_holder(client, url_v1, header, session):
    expected = "modified"
    card = credit_card_repository.create(session, obj_in=valid_visa_credit_card)

    data = valid_visa_credit_card_json.copy()
    data["holder"] = expected

    response = client.put(f"{url_v1}/credit-card/{card.id}", json=data, headers=header)
    assert response.status_code == 200
    assert response.json()["holder"] == expected


def test_update_credit_card_with_invalid_holder(client, url_v1, header, session):
    card = credit_card_repository.create(session, obj_in=valid_visa_credit_card)

    data = valid_visa_credit_card_json.copy()
    data["holder"] = "F"

    response = client.put(f"{url_v1}/credit-card/{card.id}", json=data, headers=header)
    assert response.status_code == 422
    assert response.json()["detail"]


def test_delete_credit_card(client, url_v1, header, session):
    card = credit_card_repository.create(session, obj_in=valid_visa_credit_card)

    response = client.delete(f"{url_v1}/credit-card/{card.id}", headers=header)
    assert response.status_code == 200
    assert response.json()["holder"] == valid_visa_credit_card.holder


def test_create_credit_with_payload_empty(client, url_v1, header):
    with patch(
        "app.db.repository.credit_card_repository.create",
        side_effect=Exception("mocked error"),
    ):
        with pytest.raises(Exception):
            client.post(
                f"{url_v1}/credit-card/",
                json=valid_master_credit_card_json,
                headers=header,
            )
