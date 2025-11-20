from fastapi.testclient import TestClient
from app.auth import API_TOKEN  # Use real token from app
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is working!"}


def test_create_item():
    item = {"id": 1, "name": "Laptop", "price": 999.99}

    response = client.post(
        "/items",
        json=item,
        headers={"token": API_TOKEN}
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Item created"


def test_get_item():
    # Create item before fetching
    item = {"id": 1, "name": "Laptop", "price": 999.99}
    client.post("/items", json=item, headers={"token": API_TOKEN})

    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"


def test_delete_item():
    # Create item before deleting
    item = {"id": 1, "name": "Laptop", "price": 999.99}
    client.post("/items", json=item, headers={"token": API_TOKEN})

    response = client.delete("/items/1", headers={"token": API_TOKEN})
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted"
