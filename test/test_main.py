import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture(scope="module")
def client():
    """Create a TestClient instance for testing the FastAPI app."""
    with TestClient(app) as c:
        yield c

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Math API. Visit /docs for documentation."}

def test_api_add(client):
    response = client.get("/add?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"operation": "add", "a": 10.0, "b": 5.0, "result": 15.0}

def test_api_subtract(client):
    response = client.get("/subtract?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"operation": "subtract", "a": 10.0, "b": 5.0, "result": 5.0}

def test_api_multiply(client):
    response = client.get("/multiply?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"operation": "multiply", "a": 10.0, "b": 5.0, "result": 50.0}

def test_api_divide(client):
    response = client.get("/divide?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"operation": "divide", "a": 10.0, "b": 5.0, "result": 2.0}

def test_api_divide_by_zero(client):
    response = client.get("/divide?a=10&b=0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero!"}

def test_api_add_invalid_params(client):
    response = client.get("/add?a=ten&b=five")
    assert response.status_code == 422 # Unprocessable Entity