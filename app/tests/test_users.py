from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World from FastAPI 🚀"}

def test_create_user():
    response = client.post(
        "/users/",
        json={"name": "TestUser", "email": "test@example.com"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "TestUser"
    assert data["email"] == "test@example.com"

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

