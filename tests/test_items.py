from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


FAKE_TOKEN = "abc123"


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is working!"}


def test_create_item():
    item = {
        "id": 1,
        "name": "Laptop",
        "price": 999.99
    }

    response = client.post(
        "/items",
        json=item,
        headers={"token": FAKE_TOKEN}
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Item created"


def test_get_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"


def test_delete_item():
    response = client.delete(
        "/items/1",
        headers={"token": FAKE_TOKEN}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted"
