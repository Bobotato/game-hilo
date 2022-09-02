import bcrypt
import pytest

import repository
from authentication.authenticator import authenticate, hash_password, register
from authentication.models.credentials import Credentials


def test_register(monkeypatch):
    def mock_add_entry(**kwargs):
        return "test_add_entry"

    monkeypatch.setattr(repository.user, "add_entry", mock_add_entry)
    assert (
        register(credentials=Credentials("test_username", "test_password"))
        == "test_add_entry"
    )


def test_register_raises_UsernameTakenException(monkeypatch):
    def raise_UsernameTakenException(**kwargs):
        raise repository.errors.UsernameTakenException

    monkeypatch.setattr(
        repository.user, "add_entry", raise_UsernameTakenException
    )
    with pytest.raises(repository.errors.UsernameTakenException):
        register(credentials=Credentials("test5555", "test5555"))


def test_hash_password(monkeypatch):
    def simplified_hashing(encoded_password, salt):
        return (b"salt" + encoded_password)[::-1]

    monkeypatch.setattr(bcrypt, "hashpw", simplified_hashing)

    assert hash_password("password".encode()) == "drowssaptlas".encode()


def test_authenticate(monkeypatch):
    def simplified_checking(**kwargs):
        return "checkpw"

    monkeypatch.setattr(bcrypt, "checkpw", simplified_checking)
    assert authenticate() == "checkpw"
