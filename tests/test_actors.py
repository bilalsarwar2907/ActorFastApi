from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def get_token():
    # Register a test user (ignore error if already exists)
    client.post("/auth/register", json={"username": "testuser", "password": "testpass"})
    # Login and get token
    response = client.post("/auth/login", json={"username": "testuser", "password": "testpass"})
    return response.json()["access_token"]

def test_register():
    response = client.post("/auth/register", json={"username": "newuser123", "password": "pass123"})
    assert response.status_code in [200, 400]  # 400 if already exists

def test_login():
    client.post("/auth/register", json={"username": "loginuser", "password": "pass123"})
    response = client.post("/auth/login", json={"username": "loginuser", "password": "pass123"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_wrong_password():
    response = client.post("/auth/login", json={"username": "loginuser", "password": "wrongpass"})
    assert response.status_code == 401

def test_create_actor_without_token():
    response = client.post("/actors/", json={"id": 998, "name": "No Token", "age": 25, "gender": "Male"})
    assert response.status_code == 401

def test_create_actor():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/actors/", json={"id": 999, "name": "Test Actor", "age": 30, "gender": "Male"}, headers=headers)
    assert response.status_code == 200

def test_get_all_actors():
    response = client.get("/actors/")
    assert response.status_code == 200

def test_get_actor_by_id():
    response = client.get("/actors/999")
    assert response.status_code == 200

def test_delete_actor():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.delete("/actors/999", headers=headers)
    assert response.status_code == 200