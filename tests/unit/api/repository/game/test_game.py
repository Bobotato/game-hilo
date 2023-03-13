import pytest
from sqlalchemy.exc import InvalidRequestError

from api.repository.errors import NoSuchGameException
from api.repository.game.game import GameRepository


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


def test_GameRepository_create():
    repo = GameRepository.create(session=mock_session())
    assert isinstance(repo, GameRepository)
    assert isinstance(repo._GameRepository__session, MockSession)


def test_GameRepository_get(monkeypatch):
    def mock_session_return_pickled():
        class MockSessionReturnPickled:
            def query(self, *_, **__):
                return MockQueryReturnPickled()

        class MockQueryReturnPickled:
            def filter_by(self, **_):
                return MockFilterByReturnPickled()

        class MockFilterByReturnPickled:
            def first(self):
                return {"game": "Bla"}

        return MockSessionReturnPickled()

    def mock_unpickle_object(*_):
        return "Unpickled"

    repo = GameRepository.create(session=mock_session_return_pickled())

    monkeypatch.setattr(
        "api.repository.game.game.unpickle_object", mock_unpickle_object
    )

    assert repo.get(target="test") == "Unpickled"


def test_GameRepository_get_raises_InvalidRequestError():
    def mock_session_raise_InvalidRequestError():
        class MockSessionRaiseInvalidRequestError:
            def query(self, *_, **__):
                raise InvalidRequestError

        return MockSessionRaiseInvalidRequestError()

    repo = GameRepository.create(
        session=mock_session_raise_InvalidRequestError()
    )

    with pytest.raises(InvalidRequestError):
        repo.get(target="test")


def test_GameRepository_get_raises_NoSuchGameException():
    def mock_session_return_none():
        class MockSessionReturnNone:
            def query(self, *_, **__):
                return MockQueryReturnNone()

        class MockQueryReturnNone:
            def filter_by(self, **_):
                return MockFilterByReturnNone()

        class MockFilterByReturnNone:
            def first(self):
                return

        return MockSessionReturnNone()

    repo = GameRepository.create(session=mock_session_return_none())

    with pytest.raises(NoSuchGameException):
        repo.get(target="test")
