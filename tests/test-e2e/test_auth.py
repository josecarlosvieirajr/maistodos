def test_auth_send_valid_user(client, url_v1):
    response = client.post(
        f"{url_v1}/auth/",
        json={"username": "testuser"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_auth_without_payload(client, url_v1):
    response = client.post(f"{url_v1}/auth/")

    assert response.status_code == 422
