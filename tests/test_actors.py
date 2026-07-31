from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_actor():
    response = client.post("/actors/", json={"id": 99, "name": "Test Actor", "age": 30})
    assert response.status_code == 200

def test_get_all_actors():
    response = client.get("/actors/")
    assert response.status_code == 200

def test_get_actor_by_id():
    response = client.get("/actors/99")
    assert response.status_code == 200

def test_delete_actor():
    response = client.delete("/actors/99")
    assert response.status_code == 200