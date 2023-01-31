from fastapi.testclient import TestClient
from freezegun import freeze_time

from api.main import app

client = TestClient(app)


def mock_register_user(**_):
    return 1


def mock_get_user_by_username_return_False(**_):
    return False


def mock_get_user_by_username_return_True(**_):
    return True


@freeze_time("2000-01-01")
def test_register(monkeypatch):
    monkeypatch.setattr(
        "api.router.user.user.get_user_by_username",
        mock_get_user_by_username_return_False,
    )

    monkeypatch.setattr(
        "api.router.user.user.register_user", mock_register_user
    )

    response = client.post(
        "/user/register", json={"username": "test", "password": "test"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjo5NDY2ODYwMDB9.CR_OzFi2WTQN7Y02eQXubB3rVRwyLv4JmxpkeV8vpas"  # noqa: E501
    }


def test_register_username_already_exists(monkeypatch):
    monkeypatch.setattr(
        "api.router.user.user.get_user_by_username",
        mock_get_user_by_username_return_True,
    )

    monkeypatch.setattr(
        "api.router.user.user.register_user", mock_register_user
    )

    response = client.post(
        "/user/register", json={"username": "test", "password": "test"}
    )

    assert response.status_code == 409
    assert response.json() == {
        "detail": "Account with the given username already exists"
    }


def test_register_missing_request():
    response = client.post("user/register")

    assert response.status_code == 422
