from fastapi.testclient import TestClient
from freezegun import freeze_time

from api.main import app
from api.repository.errors import NoSuchUserException

client = TestClient(app)


class MockUser:
    def __init__(self):
        self.username = "test"
        self.password_hash = (
            "$2b$12$ol/TcrgrOS.0WqJaQXdEWeBomfSLWHvNJEocZIJewS2FNaxJBNhx2"
        )


def mock_get_user_by_username(*args, **kwargs):
    return MockUser()


@freeze_time("2000-01-01")
def test_authenticate(monkeypatch):
    monkeypatch.setattr(
        "api.router.user.user.get_user_by_username", mock_get_user_by_username
    )

    response = client.post(
        "/user/authenticate", json={"username": "test", "password": "test"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjo5NDY2ODYwMDB9.CR_OzFi2WTQN7Y02eQXubB3rVRwyLv4JmxpkeV8vpas"  # noqa: E501
    }


def test_authenticate_invalid_password(monkeypatch):
    monkeypatch.setattr(
        "api.router.user.user.get_user_by_username", mock_get_user_by_username
    )

    response = client.post(
        "/user/authenticate", json={"username": "test", "password": "nottest"}
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Password does not match the given username."
    }


def test_authenticate_missing_user_return_NoSuchUserException(monkeypatch):
    def mock_get_user_by_username_return_NoSuchUserException(*args, **kwargs):
        raise NoSuchUserException

    monkeypatch.setattr(
        "api.router.user.user.get_user_by_username",
        mock_get_user_by_username_return_NoSuchUserException,
    )

    response = client.post(
        "/user/authenticate",
        json={"username": "doesnotexist", "password": "test"},
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "User does not exist."}


def test_authenticate_missing_request():
    response = client.post("/user/authenticate")

    assert response.status_code == 422
