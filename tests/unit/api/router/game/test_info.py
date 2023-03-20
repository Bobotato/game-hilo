from fastapi.testclient import TestClient
from freezegun import freeze_time

from api.main import app
from api.repository.pickler import pickle_object

client = TestClient(app)


class MockGame:
    def __init__(self, **_):
        pass

    def start_round(self, **_):
        return {
            "player": {"name": "test", "credits": 100},
            "current_card": {"sort_index": 1, "rank": 1, "suit": 2},
        }


mock_game = MockGame()
pickled_mock_game = pickle_object(mock_game)


class MockUser:
    def __init__(self, mock_game):
        self.username = "test"
        self.game = mock_game


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


def mock_update_game(**_):
    return "updated"


def mock_update_round_info(**_):
    return "updated"


@freeze_time("2000-01-01")
def test_info(monkeypatch):
    def mock_get_user_from_token_return_MockUser(**_):
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
        "/game/info",
        json={
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjo5NDY2ODYwMDB9.CR_OzFi2WTQN7Y02eQXubB3rVRwyLv4JmxpkeV8vpas"  # noqa: E501
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "player": {"name": "test", "credits": 100},
        "current_card": {"sort_index": 1, "rank": 1, "suit": 2},
    }


@freeze_time("2000-01-01")
def test_info_no_game(monkeypatch):
    def mock_get_user_from_token_return_MockUserNoGame(**_):
        return MockUserNoGame()

    monkeypatch.setattr(
        "api.router.game.game.get_user_from_token",
        mock_get_user_from_token_return_MockUserNoGame,
    )

    monkeypatch.setattr("api.router.game.game.update_game", mock_update_game)
    monkeypatch.setattr(
        "api.router.game.game.update_round_info", mock_update_round_info
    )

    monkeypatch.setattr("api.router.game.game.Game", MockGame)

    response = client.post(
        "/game/info",
        json={
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjo5NDY2ODYwMDB9.CR_OzFi2WTQN7Y02eQXubB3rVRwyLv4JmxpkeV8vpas"  # noqa: E501
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "player": {"name": "test", "credits": 100},
        "current_card": {"sort_index": 1, "rank": 1, "suit": 2},
    }
