from fastapi.testclient import TestClient
from freezegun import freeze_time
from sqlalchemy.exc import InvalidRequestError

from api.main import app
from api.repository.errors import NoSuchUserException
from api.router import error_codes

client = TestClient(app)


@freeze_time("2000-01-01")
def test_authenticate(monkeypatch):
    def mock_verify_password_return_true(**_):
        return True

    def mock_create_access_token(**_):
        return "test_token"

    monkeypatch.setattr(
        "api.router.user.user.verify_password",
        mock_verify_password_return_true,
    )

    monkeypatch.setattr(
        "api.router.user.user.create_access_token",
        mock_create_access_token,
    )

    response = client.post(
        "/user/authenticate", json={"username": "test", "password": "test"}
    )

    assert response.status_code == 200
    assert response.json() == {"access_token": "test_token"}


@freeze_time("2000-01-01")
def test_authenticate_invalid_password_return_401(monkeypatch):
    def mock_verify_password_return_false(**_):
        return False

    monkeypatch.setattr(
        "api.router.user.user.verify_password",
        mock_verify_password_return_false,
    )

    response = client.post(
        "/user/authenticate", json={"username": "test", "password": "nottest"}
    )

    assert response.status_code == 401
    assert response.json() == {
        "error_code": error_codes.INVALID_CREDENTIALS,
        "detail": "The credentials input were invalid.",
    }


@freeze_time("2000-01-01")
def test_authenticate_no_such_user_return_401(monkeypatch):
    def mock_verify_password_return_NoSuchUserException(**_):
        raise NoSuchUserException

    monkeypatch.setattr(
        "api.router.user.user.verify_password",
        mock_verify_password_return_NoSuchUserException,
    )

    response = client.post(
        "/user/authenticate",
        json={"username": "doesnotexist", "password": "test"},
    )

    assert response.status_code == 401
    assert response.json() == {
        "error_code": error_codes.INVALID_CREDENTIALS,
        "detail": "The credentials input were invalid.",
    }


def test_authenticate_invalid_request_return_400(monkeypatch):
    def mock_verify_password_return_InvalidRequestError(**_):
        raise InvalidRequestError

    monkeypatch.setattr(
        "api.router.user.user.verify_password",
        mock_verify_password_return_InvalidRequestError,
    )

    response = client.post(
        "/user/authenticate", json={"username": "", "password": ""}
    )

    assert response.status_code == 400
    assert response.json() == {
        "error_code": error_codes.INVALID_REQUEST,
        "detail": "The request was invalid.",
    }
