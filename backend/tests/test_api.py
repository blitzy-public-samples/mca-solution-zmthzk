import pytest
from fastapi.testclient import TestClient
from main import app
from models import User, Application, Webhook
from database import get_db

client = TestClient(app)

@pytest.fixture
def db_session():
    # Setup test database session
    db = next(get_db())
    yield db
    db.close()

# Test cases for authentication endpoints
def test_register_user(db_session):
    response = client.post("/auth/register", json={"username": "testuser", "email": "test@example.com", "password": "testpass"})
    assert response.status_code == 201
    assert "id" in response.json()

def test_login_user(db_session):
    # First register a user
    client.post("/auth/register", json={"username": "loginuser", "email": "login@example.com", "password": "loginpass"})
    
    # Then try to login
    response = client.post("/auth/login", data={"username": "loginuser", "password": "loginpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()

# Test cases for application management endpoints
def test_create_application(db_session):
    # Login first to get the token
    login_response = client.post("/auth/login", data={"username": "loginuser", "password": "loginpass"})
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/applications", json={"name": "Test App", "description": "Test Description"}, headers=headers)
    assert response.status_code == 201
    assert "id" in response.json()

def test_get_applications(db_session):
    # Login first to get the token
    login_response = client.post("/auth/login", data={"username": "loginuser", "password": "loginpass"})
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/applications", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test cases for webhook management endpoints
def test_create_webhook(db_session):
    # Login first to get the token
    login_response = client.post("/auth/login", data={"username": "loginuser", "password": "loginpass"})
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # Create an application first
    app_response = client.post("/applications", json={"name": "Webhook App", "description": "For webhook testing"}, headers=headers)
    app_id = app_response.json()["id"]
    
    # Create a webhook
    response = client.post(f"/applications/{app_id}/webhooks", json={"url": "https://example.com/webhook", "events": ["user.created"]}, headers=headers)
    assert response.status_code == 201
    assert "id" in response.json()

def test_get_webhooks(db_session):
    # Login first to get the token
    login_response = client.post("/auth/login", data={"username": "loginuser", "password": "loginpass"})
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # Get the application id
    app_response = client.get("/applications", headers=headers)
    app_id = app_response.json()[0]["id"]
    
    response = client.get(f"/applications/{app_id}/webhooks", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test cases for error handling and edge cases
def test_login_with_invalid_credentials():
    response = client.post("/auth/login", data={"username": "invaliduser", "password": "invalidpass"})
    assert response.status_code == 401

def test_create_application_without_auth():
    response = client.post("/applications", json={"name": "Unauthorized App", "description": "This should fail"})
    assert response.status_code == 401

def test_get_non_existent_application(db_session):
    # Login first to get the token
    login_response = client.post("/auth/login", data={"username": "loginuser", "password": "loginpass"})
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/applications/99999", headers=headers)
    assert response.status_code == 404

# HUMAN ASSISTANCE NEEDED
# The following test case might need adjustments based on the actual implementation of rate limiting
def test_rate_limiting():
    # Implement rate limiting test
    pass

# HUMAN ASSISTANCE NEEDED
# The following test case needs to be implemented based on the actual error responses
def test_error_response_format():
    # Test that error responses follow a consistent format
    pass