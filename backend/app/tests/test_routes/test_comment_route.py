def test_get_comments(client):
    response = client.get("/v1/comments/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_comment_route(client):
    task_id = client.post("/v1/tasks/", json={"title": "Task"}).json()
    payload = {"task_id": task_id, "description": "C"}
    response = client.post("/v1/comments/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, int)

def test_get_comment_route(client):
    task_id = client.post("/v1/tasks/", json={"title": "Task"}).json()
    comment_id = client.post("/v1/comments/", json={"task_id": task_id, "description": "C"}).json()
    response = client.get(f"/v1/comments/{comment_id}/")
    assert response.status_code == 200
    assert response.json()["id"] == comment_id

def test_delete_comment_route(client):
    task_id = client.post("/v1/tasks/", json={"title": "Task"}).json()
    comment_id = client.post("/v1/comments/", json={"task_id": task_id, "description": "C"}).json()
    response = client.delete(f"/v1/comments/{comment_id}/")
    assert response.status_code == 200
