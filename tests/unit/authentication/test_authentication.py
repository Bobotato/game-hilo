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
    def simplified_hashing(encoded_password, salt):
        return (b"salt" + encoded_password)[::-1]

    monkeypatch.setattr(bcrypt, "hashpw", simplified_hashing)

    assert hash_password("password".encode()) == "drowssaptlas".encode()


def test_authenticate(monkeypatch):
    def simplified_checking(*args, **kwargs):
        return "checkpw"

    monkeypatch.setattr(bcrypt, "checkpw", simplified_checking)
    assert authenticate(Credentials("test", "testpw")) == "checkpw"
