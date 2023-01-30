from fastapi.testclient import TestClient
from freezegun import freeze_time

from api.main import app
from api.repository.pickler import pickle_object

client = TestClient(app)


class MockGame:
    def __init__(self, *args, **kwargs):
        pass

    def start_round(self, *args, **kwargs):
        return {
            "player": {"name": "test", "credits": 100},
            "current_card": {"sort_index": 1, "rank": 1, "suit": 2},
        }

    def compute_round_result(self, *args, **kwargs):
        return {
            "drawn_card": {"sort_index": 1, "rank": 1, "suit": 1},
            "win": True,
            "is_player_bankrupt": False,
            "is_deck_empty": False,
        }


mock_game = MockGame()
pickled_mock_game = pickle_object(mock_game)


class MockUser:
    def __init__(self, mock_game):
        self.username = "test"
        self.game = mock_game
        self.round_info = "test"


class MockUserNoGame:
    def __init__(self):
        self.username = "test"
        self.game = None
        self.round_info = "testroundinfo"


class MockUserNoRoundInfo:
    def __init__(self):
        self.username = "test"
        self.game = "testgame"
        self.round_info = None


def mock_update_game(*args, **kwargs):
    return "updated"


def mock_update_round_info(*args, **kwargs):
    return "updated"


@freeze_time("2000-01-01")
def test_result(monkeypatch):
    def mock_get_user_from_token_return_MockUser(*args, **kwargs):
        return MockUser(mock_game=pickled_mock_game)

    monkeypatch.setattr(
        "api.router.game.game.get_user_from_token",
        mock_get_user_from_token_return_MockUser,
    )

    monkeypatch.setattr("api.router.game.game.update_game", mock_update_game)
    monkeypatch.setattr(
        "api.router.game.game.update_round_info", mock_update_round_info
    )

    response = client.post(
        "game/result?bet=50&prediction=1",
        json={
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjo5NDY2ODYwMDB9.CR_OzFi2WTQN7Y02eQXubB3rVRwyLv4JmxpkeV8vpas"  # noqa: E501
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "drawn_card": {"sort_index": 1, "rank": 1, "suit": 1},
        "win": True,
        "is_player_bankrupt": False,
        "is_deck_empty": False,
    }


@freeze_time("2000-01-01")
def test_result_missing_game_return_HTTPException(monkeypatch):
    def mock_get_user_from_token_return_None(*args, **kwargs):
        return MockUserNoGame()

    monkeypatch.setattr(
        "api.router.game.game.get_user_from_token",
        mock_get_user_from_token_return_None,
    )

    response = client.post(
        "/game/result?bet=50&prediction=1",
        json={
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjo5NDY2ODYwMDB9.CR_OzFi2WTQN7Y02eQXubB3rVRwyLv4JmxpkeV8vpas"  # noqa: E501
        },
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "There is no game associated with this player."
    }


@freeze_time("2000-01-01")
def test_result_missing_round_info(monkeypatch):
    def mock_get_user_from_token_no_round_info(*args, **kwargs):
        return MockUserNoRoundInfo()

    monkeypatch.setattr(
        "api.router.game.game.get_user_from_token",
        mock_get_user_from_token_no_round_info,
    )

    response = client.post(
        "/game/result?bet=50&prediction=1",
        json={
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjo5NDY2ODYwMDB9.CR_OzFi2WTQN7Y02eQXubB3rVRwyLv4JmxpkeV8vpas"  # noqa: E501
        },
    )

    assert response.status_code == 403
    assert response.json() == {
        "detail": "Round info does not exist, start a round first."
    }
