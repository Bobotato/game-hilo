import pytest
from freezegun import freeze_time
from sqlalchemy.exc import InvalidRequestError

from api.repository.errors import (
    GenericException,
    NoSuchUserException,
    UsernameTakenException,
)
from api.services.user.user import create_token, register_user, verify_password


class MockUserRepository:
    @classmethod
    def create(cls, *_):
        return cls()

    def get(self, **_):
        class PasswordHash:
            def __init__(self):
                self.password_hash = "$2b$12$BfakHwThl4HooCXFceIbKujE7SOg.Wt1NR76tuS1jxxSKiSj/Yx2O"  # noqa: E501

        return PasswordHash()


class MockUserRepositoryGetRaisesGenericException:
    @classmethod
    def create(cls, *_):
        return cls()

    def add(self, *_, **__):
        raise SuccessException

    def get(self, **_):
        raise GenericException


class MockUserRepositoryGetRaisesInvalidRequestError:
    @classmethod
    def create(cls, *_):
        return cls()

    def add(self, *_, **__):
        raise SuccessException

    def get(self, **_):
        raise InvalidRequestError


class MockUserRepositoryUsernameTaken:
    @classmethod
    def create(cls, *_):
        return cls()

    def get(self, **_):
        return "Username Exists"


class SuccessException(Exception):
    def __str__(self):
        return "The user was registered."


def mock_credentials():
    class MockCredentials:
        def __init__(self):
            self.username = "test"
            self.password = "test"

    return MockCredentials()


def mock_session():
    class MockSession:
        pass

    return MockSession()


@freeze_time("2000-01-01")
def test_create_token():
    assert (
        create_token(credentials=mock_credentials())
        == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjo5NDY2ODYwMDB9.CR_OzFi2WTQN7Y02eQXubB3rVRwyLv4JmxpkeV8vpas"  # noqa: E501
    )


def test_register_user(monkeypatch):
    monkeypatch.setattr(
        "api.services.user.user.UserRepository",
        MockUserRepositoryGetRaisesGenericException,
    )

    with pytest.raises(SuccessException):
        register_user(credentials=mock_credentials(), db=mock_session())


def test_register_user_raises_username_taken_exception(
    monkeypatch,
):
    monkeypatch.setattr(
        "api.services.user.user.UserRepository",
        MockUserRepositoryUsernameTaken,
    )

    with pytest.raises(UsernameTakenException):
        register_user(credentials=mock_credentials(), db=mock_session())


def test_verify_password(monkeypatch):
    monkeypatch.setattr(
        "api.services.user.user.UserRepository", MockUserRepository
    )

    assert (
        verify_password(credentials=mock_credentials(), db=mock_session())
        is True
    )


def test_verify_password_invalid_request_raises_invalid_request_error(
    monkeypatch,
):
    monkeypatch.setattr(
        "api.services.user.user.UserRepository",
        MockUserRepositoryGetRaisesInvalidRequestError,
    )

    with pytest.raises(InvalidRequestError):
        verify_password(credentials=mock_credentials(), db=mock_session())


def test_verify_password_no_such_user_raises_no_such_user_exception(
    monkeypatch,
):
    monkeypatch.setattr(
        "api.services.user.user.UserRepository",
        MockUserRepositoryGetRaisesGenericException,
    )

    with pytest.raises(NoSuchUserException):
        verify_password(credentials=mock_credentials(), db=mock_session())
