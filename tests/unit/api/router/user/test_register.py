from fastapi.testclient import TestClient

from api.main import app
from api.repository.errors import UsernameTakenException
from api.router import error_codes

client = TestClient(app)


def test_register(monkeypatch):
    def mock_register_user(**_):
        return

    def mock_create_access_token(**_):
        return "test_token"

    monkeypatch.setattr(
        "api.router.user.user.register_user", mock_register_user
    )

    monkeypatch.setattr(
        "api.router.user.user.create_access_token", mock_create_access_token
    )

    response = client.post(
        "/user/register", json={"username": "test", "password": "test"}
    )

    assert response.status_code == 200
    assert response.json() == {"access_token": "test_token"}


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
