def test_read_health(client, url_v1):
    response = client.get(f"{url_v1}/health/")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}
