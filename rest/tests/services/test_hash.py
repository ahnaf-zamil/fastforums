from fastapi.testclient import TestClient
from app.main import app
from app.services.hash import HashService

import pytest


@pytest.fixture
def test_client():
    yield TestClient(app)


@pytest.fixture
def hash_service():
    yield HashService()


def test_hash_password(test_client: TestClient, hash_service: HashService):
    password = "test12345"

    hashed_pw = hash_service.get_password_hash(password)
    assert hash_service.verify_password(password, hashed_pw)
