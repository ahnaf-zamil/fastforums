from fastapi.testclient import TestClient
from app.main import app
from app.utils.database import get_db
from app.services.user import UserService
from app.services.hash import HashService
from uuid import UUID

import pytest


@pytest.fixture
def test_client():
    yield TestClient(app)


@pytest.fixture
def hash_service():
    yield HashService()


@pytest.fixture
def user_service():
    yield UserService(get_db())


def test_create_user(
    test_client: TestClient, hash_service: HashService, user_service: UserService
):
    response = test_client.post(
        "/users/create",
        json={"username": "test", "email": "test@gmail.com", "password": "test12345"},
    )
    assert response.status_code == 200, response.text

    data = response.json()

    assert data["username"] == "test"
    assert data["email"] == "test@gmail.com"

    assert "id" in data  # Checking if ID exists
    assert UUID(data["id"]).hex == data["id"].replace(
        "-", ""
    )  # Checking if ID hex matches

    user = user_service.get_user_by_id(data["id"])  # Service result value

    assert user.id == data["id"]
    assert user.email == "test@gmail.com"
    assert user.username == "test"
    assert hash_service.verify_password("test12345", user.password)


def test_invalid_payload_create_user(test_client: TestClient):
    response = test_client.post(
        "/users/create",
        json={"username": "te", "email": "test@gmail.com", "password": "test12345"},
    )  # Bad username
    assert response.status_code == 422, response.text

    response = test_client.post(
        "/users/create",
        json={"username": "test", "email": "testgmail.com", "password": "test12345"},
    )  # Bad email
    assert response.status_code == 422, response.text

    response = test_client.post(
        "/users/create",
        json={"username": "test", "email": "test@gmail.com", "password": "123"},
    )  # Bad password
    assert response.status_code == 422, response.text


def test_login_user(test_client: TestClient, user_service: UserService):
    response = test_client.post(
        "/users/login", json={"email": "test@gmail.com", "password": "test12345"}
    )
    assert response.status_code == 200, response.text

    data = response.json()

    # Verifying return payload
    assert data["email"] == "test@gmail.com"
    assert data["username"] == "test"  # Since the registered user is test
    assert "id" in data  # Checking if ID exists
    assert UUID(data["id"]).hex == data["id"].replace(
        "-", ""
    )  # Checking if ID hex matches

    # Verifying session cookie
    assert response.cookies["session"]
    assert UUID(response.cookies["session"]).hex == response.cookies["session"].replace(
        "-", ""
    )


def test_invalid_cred_login_user(test_client: TestClient):
    # Wrong password
    response = test_client.post(
        "/users/login", json={"email": "test@gmail.com", "password": "wrongpassword"}
    )
    assert response.status_code == 401, response.text

    data = response.json()
    assert "description" in data

    # Wrong email
    response = test_client.post(
        "/users/login", json={"email": "wrongemail@gmail.com", "password": "test12345"}
    )
    assert response.status_code == 401, response.text

    data = response.json()
    assert "description" in data


def test_get_user(test_client: TestClient):
    # Logging in
    login_response = test_client.post(
        "/users/login", json={"email": "test@gmail.com", "password": "test12345"}
    )
    assert login_response.status_code == 200, login_response.text

    response = test_client.get("/users/@me")
    assert response.status_code == 200, response.text

    data = response.json()

    assert data["username"] == "test"
    assert data["email"] == "test@gmail.com"


def test_not_logged_in_get_user(test_client: TestClient):
    response = test_client.get("/users/@me")
    assert response.status_code == 401, response.text

    data = response.json()

    assert "description" in data
