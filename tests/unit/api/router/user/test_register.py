from fastapi.testclient import TestClient
from freezegun import freeze_time

from api.main import app
from api.repository.errors import UsernameTakenException
from api.router import error_codes

client = TestClient(app)


@freeze_time("2000-01-01")
def test_register(monkeypatch):
    def mock_register_user(**_):
        return 1

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


def test_register_username_taken_return_409(monkeypatch):
    def mock_get_user_by_username_raise_UsernameTakenException(**_):
        raise UsernameTakenException

    monkeypatch.setattr(
        "api.router.user.user.register_user",
        mock_get_user_by_username_raise_UsernameTakenException,
    )

    response = client.post(
        "/user/register", json={"username": "test", "password": "test"}
    )

    assert response.status_code == 409
    assert response.json() == {
        "error_code": error_codes.USERNAME_TAKEN,
        "detail": "The username has already been taken.",
    }
