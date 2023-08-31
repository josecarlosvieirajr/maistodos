def test_read_health(client):
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}
