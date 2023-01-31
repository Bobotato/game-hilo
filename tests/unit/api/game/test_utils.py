import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient
from freezegun import freeze_time

from api.main import app
from api.repository.errors import NoSuchUserException
from api.router.game.utils import get_user_from_token

client = TestClient(app)


class ValidToken:
    def __init__(self):
        self.access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjoxNjc1MTUwMjI0fQ.Nc939a1gp0-u2sB9UwS_gzxINjRkicQKj_8PWVuGlTs"  # noqa: E501


test_token = ValidToken()


@freeze_time("2000-01-01")
def test_get_user_from_token(monkeypatch):
    def mock_get_user_by_username_return_MockUser(**_):
        return "user"

    monkeypatch.setattr(
        "api.router.game.utils.get_user_by_username",
        mock_get_user_by_username_return_MockUser,
    )

    assert get_user_from_token(token=test_token, db="db") == "user"


@freeze_time("2000-01-01")
def test_get_user_from_token_no_user_raise_NoSuchUserException(monkeypatch):
    def mock_get_user_by_username_raise_NoSuchUserException(**_):
        raise NoSuchUserException

    monkeypatch.setattr(
        "api.router.game.utils.get_user_by_username",
        mock_get_user_by_username_raise_NoSuchUserException,
    )

    with pytest.raises(HTTPException):
        get_user_from_token(token=test_token, db="db")
