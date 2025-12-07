def test_login(client):
    payload = {"username": "admin", "password": "admin", "grant_type": "password"}
    response = client.post("/api/v1/users/token/", data=payload)
    assert response.status_code == 200
    token_json = response.json()
    assert "access_token" in token_json


def test_wrong_login(client):
    payload = {"username": "admin", "password": "123", "grant_type": "password"}
    response = client.post("/api/v1/users/token/", data=payload)
    assert response.status_code == 401
    assert "WWW-Authenticate" in response.headers