import pytest
from sqlalchemy.exc import InvalidRequestError

from api.repository.errors import NoSuchUserException
from api.repository.user.user import UserRepository


class MockSession:
    def query(self, *_, **__):
        return MockQuery()


class MockQuery:
    def filter_by(self, **_):
        return MockFilterBy()


class MockFilterBy:
    def first(self):
        return "First of filtered query"


def mock_session():
    return MockSession()


def test_UserRepository_create():
    repo = UserRepository.create(session=mock_session())
    assert isinstance(repo, UserRepository)
    assert isinstance(repo._UserRepository__session, MockSession)


def test_UserRepository_get():
    repo = UserRepository.create(session=mock_session())
    assert repo.get(target="test", filter="test") == "First of filtered query"


def test_UserRepository_get_raises_InvalidRequestError():
    def mock_session_raise_InvalidRequestError():
        class MockSessionRaiseInvalidRequestError:
            def query(self, *_, **__):
                raise InvalidRequestError

        return MockSessionRaiseInvalidRequestError()

    repo = UserRepository.create(
        session=mock_session_raise_InvalidRequestError()
    )

    with pytest.raises(InvalidRequestError):
        repo.get(target="test")


def test_UserRepository_get_raises_NoSuchUserException():
    def mock_session_raise_NoSuchUserException():
        class MockSessionRaiseNoSuchUserException:
            def query(self, *_, **__):
                raise NoSuchUserException

        return MockSessionRaiseNoSuchUserException()

    repo = UserRepository.create(
        session=mock_session_raise_NoSuchUserException()
    )

    with pytest.raises(NoSuchUserException):
        repo.get(target="test")
