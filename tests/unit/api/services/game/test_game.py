import pytest
from freezegun import freeze_time

from api.repository.errors import GenericException, NoSuchGameException
from api.services.game.game import (
    create_game_state,
    get_game_object,
    get_info,
    get_result,
    get_username_from_token,
    update_game,
)


class SuccessfullyAddedException(Exception):
    pass


class SuccessfullyPatchedException(Exception):
    pass


def mock_create_game_state(**_):
    return


def mock_game(**_):
    class MockGame:
        def start_round(*_):
            return "Started without pre-existing game"

    return MockGame()


def mock_game_repository():
    class MockGameRepository:
        def add(self, **_):
            raise SuccessfullyAddedException

        def get(self, **_):
            return "Get success without create method"

        def patch(self, **_):
            raise SuccessfullyPatchedException

    return MockGameRepository()


def mock_game_repository_return_GenericException():
    class MockGameRepositoryReturnGenericException:
        def get(self, **_):
            raise GenericException

    return MockGameRepositoryReturnGenericException()


class MockGameRepositorywithCreateClassMethod:
    @classmethod
    def create(cls, *_):
        return cls()

    def get(self, **_):
        return "Get success with create method"


def mock_get_game_object(**_):
    class MockGame:
        def start_round(self, *_):
            return "Started"

        def compute_round_result(self, **_):
            return "Computed"

    return MockGame()


def mock_get_game_object_raise_NoSuchGameException(**_):
    raise NoSuchGameException


def mock_get_username_from_token(**_):
    return "test"


def mock_pickle_object(*_):
    return "Pickled"


def mock_session():
    class MockSession:
        pass

    return MockSession()


def mock_token():
    class TestToken:
        def __init__(self):
            self.access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjo5NDY2ODYwMDB9.CR_OzFi2WTQN7Y02eQXubB3rVRwyLv4JmxpkeV8vpas"  # noqa: E501

    return TestToken()


def mock_update_game(**_):
    return


def test_create_game_state():
    with pytest.raises(SuccessfullyAddedException):
        create_game_state(username="test", repo=mock_game_repository())


def test_get_game_object():
    assert (
        get_game_object(username="test", repo=mock_game_repository())
        == "Get success without create method"
    )


def test_get_game_object_no_such_game_returns_NoSuchGameException():
    with pytest.raises(NoSuchGameException):
        get_game_object(
            username="test",
            repo=mock_game_repository_return_GenericException(),
        )


def test_get_info_with_existing_game(monkeypatch):
    monkeypatch.setattr(
        "api.services.game.game.GameRepository",
        MockGameRepositorywithCreateClassMethod,
    )
    monkeypatch.setattr(
        "api.services.game.game.get_username_from_token",
        mock_get_username_from_token,
    )
    monkeypatch.setattr(
        "api.services.game.game.get_game_object", mock_get_game_object
    )
    monkeypatch.setattr("api.services.game.game.update_game", mock_update_game)

    assert get_info(token=mock_token(), db=mock_session()) == "Started"


def test_get_info_without_existing_game(monkeypatch):
    monkeypatch.setattr(
        "api.services.game.game.GameRepository",
        MockGameRepositorywithCreateClassMethod,
    )
    monkeypatch.setattr(
        "api.services.game.game.get_username_from_token",
        mock_get_username_from_token,
    )
    monkeypatch.setattr(
        "api.services.game.game.get_game_object",
        mock_get_game_object_raise_NoSuchGameException,
    )
    monkeypatch.setattr(
        "api.services.game.game.create_game_state", mock_create_game_state
    )
    monkeypatch.setattr("api.services.game.game.Game", mock_game)
    monkeypatch.setattr("api.services.game.game.update_game", mock_update_game)

    assert (
        get_info(token=mock_token(), db=mock_session())
        == "Started without pre-existing game"
    )


@freeze_time("2000-01-01")
def test_get_result(monkeypatch):
    monkeypatch.setattr(
        "api.services.game.game.GameRepository",
        MockGameRepositorywithCreateClassMethod,
    )
    monkeypatch.setattr(
        "api.services.game.game.get_game_object", mock_get_game_object
    )
    monkeypatch.setattr("api.services.game.game.update_game", mock_update_game)

    assert (
        get_result(bet=1, prediction=1, token=mock_token(), db=mock_session())
        == "Computed"
    )


@freeze_time("2000-01-01")
def test_get_result_no_such_game_returns_NoSuchGameException(monkeypatch):
    monkeypatch.setattr(
        "api.services.game.game.GameRepository",
        MockGameRepositorywithCreateClassMethod,
    )
    monkeypatch.setattr(
        "api.services.game.game.get_game_object",
        mock_get_game_object_raise_NoSuchGameException,
    )
    with pytest.raises(NoSuchGameException):
        get_result(bet=1, prediction=1, token=mock_token(), db=mock_session())


@freeze_time("2000-01-01")
def test_get_username_from_token():
    assert get_username_from_token(token=mock_token()) == "test"


def test_update_game(monkeypatch):
    monkeypatch.setattr(
        "api.services.game.game.pickle_object", mock_pickle_object
    )

    with pytest.raises(SuccessfullyPatchedException):
        update_game(
            username="test", game=mock_game(), repo=mock_game_repository()
        )