import bcrypt
import pytest

from authentication.authenticator import authenticate, hash_password, register
from authentication.models.credentials import Credentials
from repository.errors import UsernameTakenException


def test_register_raises_UsernameTakenException(monkeypatch):
    def raise_UsernameTakenException(**kwargs):
        raise UsernameTakenException

    monkeypatch.setattr(
        "authentication.authenticator.add_entry", raise_UsernameTakenException
    )
    with pytest.raises(UsernameTakenException):
        register(credentials=Credentials("test_username", "test_password"))


def test_hash_password(monkeypatch):
    def mock_hashing(encoded_password, salt):
        return (b"salt" + encoded_password)[::-1]

    monkeypatch.setattr(bcrypt, "hashpw", mock_hashing)

    assert hash_password("password".encode()) == "drowssaptlas".encode()


def test_authenticate(monkeypatch):
    def mock_checking(*args, **kwargs):
        return "check_pw"

    def mock_get_entry(*args, **kwargs):
        class MockUser:
            password_hash = "testpw"

        return MockUser

    monkeypatch.setattr(bcrypt, "checkpw", mock_checking)
    monkeypatch.setattr(
        "authentication.authenticator.get_entry", mock_get_entry
    )

    assert authenticate(Credentials("test", "testpw")) == "check_pw"
