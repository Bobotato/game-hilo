import bcrypt
import pytest

from authentication.authenticator import authenticate, hash_password, register
from authentication.models.credentials import Credentials
from repository.errors import UsernameTakenException
from repository.models.user import User


def test_register_raises_UsernameTakenException(monkeypatch):
    def raise_UsernameTakenException(**_):
        raise UsernameTakenException

    monkeypatch.setattr(
        "authentication.authenticator.add_entry", raise_UsernameTakenException
    )
    with pytest.raises(UsernameTakenException):
        register(credentials=Credentials("test_username", "test_password"))


def test_hash_password(monkeypatch):
    def mock_salt_generation():
        return b"$2b$12$PLiYfdCEt70UukCL5m1li."

    monkeypatch.setattr(bcrypt, "gensalt", mock_salt_generation)

    assert (
        hash_password("password")
        == "$2b$12$PLiYfdCEt70UukCL5m1li.1nLlQqZcv1qKSyel1DEjpIl0Tk0Keqi"
    )


def test_authenticate(monkeypatch):
    def mock_get_entry(**_):
        return User(
            "test_username",
            "$2b$12$PLiYfdCEt70UukCL5m1li.1nLlQqZcv1qKSyel1DEjpIl0Tk0Keqi",
        )

    monkeypatch.setattr(
        "authentication.authenticator.get_entry", mock_get_entry
    )

    assert authenticate(Credentials("test_username", "password"))
