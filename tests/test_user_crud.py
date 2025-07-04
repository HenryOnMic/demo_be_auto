import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    user_data = {"name": "Alice", "email": "alice@example.com", "age": 30}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]
    assert data["age"] == user_data["age"]
    assert "id" in data 

def test_get_user_by_id():
    # First, create a user
    user_data = {"name": "Bob", "email": "bob@example.com", "age": 25}
    create_resp = client.post("/users/", json=user_data)
    user_id = create_resp.json()["id"]

    # Now, get the user by id
    get_resp = client.get(f"/users/{user_id}")
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["id"] == user_id
    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]
    assert data["age"] == user_data["age"] 

def test_list_users():
    user1 = {"name": "Carol", "email": "carol@example.com", "age": 22}
    user2 = {"name": "Dave", "email": "dave@example.com", "age": 28}
    resp1 = client.post("/users/", json=user1)
    resp2 = client.post("/users/", json=user2)
    list_resp = client.get("/users/")
    assert list_resp.status_code == 200
    data = list_resp.json()
    assert isinstance(data, list)
    assert len(data) == 2
    emails = [u["email"] for u in data]
    assert user1["email"] in emails
    assert user2["email"] in emails 

def test_update_user():
    user_data = {"name": "Eve", "email": "eve@example.com", "age": 40}
    create_resp = client.post("/users/", json=user_data)
    user_id = create_resp.json()["id"]
    update_data = {"name": "Eve Updated", "email": "eve@example.com", "age": 41}
    update_resp = client.put(f"/users/{user_id}", json=update_data)
    assert update_resp.status_code == 200
    data = update_resp.json()
    assert data["id"] == user_id
    assert data["name"] == update_data["name"]
    assert data["email"] == update_data["email"]
    assert data["age"] == update_data["age"] 

def test_delete_user():
    user_data = {"name": "Frank", "email": "frank@example.com", "age": 50}
    create_resp = client.post("/users/", json=user_data)
    user_id = create_resp.json()["id"]
    delete_resp = client.delete(f"/users/{user_id}")
    assert delete_resp.status_code == 204
    # Confirm user is gone
    get_resp = client.get(f"/users/{user_id}")
    assert get_resp.status_code == 404 