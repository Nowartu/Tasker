def test_get_tasks(client):
    response = client.get("/v1/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_task_route(client):
    payload = {"title": "Task", "description": "Desc"}
    response = client.post("/v1/tasks/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, int)

def test_get_task_route(client):
    payload = {"title": "Task"}
    task_id = client.post("/v1/tasks/", json=payload).json()
    response = client.get(f"/v1/tasks/{task_id}/")
    assert response.status_code == 200
    assert response.json()["id"] == task_id

def test_update_task_route(client):
    payload = {"title": "Task"}
    task_id = client.post("/v1/tasks/", json=payload).json()
    update_payload = {"id": task_id, "done": True, "done_by": "user1"}
    response = client.put(f"/v1/tasks/{task_id}", json=update_payload)
    assert response.status_code == 200

def test_delete_task_route(client):
    payload = {"title": "Task"}
    task_id = client.post("/v1/tasks/", json=payload).json()
    response = client.delete(f"/v1/tasks/{task_id}")
    assert response.status_code == 200
    response = client.get(f"/v1/tasks/{task_id}/")
    assert response.status_code == 404
