from fastapi.testclient import TestClient
from jose import ExpiredSignatureError, JWTError

from api.main import app
from api.repository.errors import NoSuchGameException
from api.router import error_codes

client = TestClient(app)


def test_result(monkeypatch):
    def mock_get_result(**_):
        return {
            "drawn_card": {"sort_index": 1, "rank": 1, "suit": 1},
            "win": True,
            "is_player_bankrupt": False,
            "is_deck_empty": False,
        }

    monkeypatch.setattr(
        "api.router.game.game.get_result",
        mock_get_result,
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


def test_result_expired_token_return_401(monkeypatch):
    def mock_get_result_raise_ExpiredSignatureError(**_):
        raise ExpiredSignatureError

    monkeypatch.setattr(
        "api.router.game.game.get_result",
        mock_get_result_raise_ExpiredSignatureError,
    )

    response = client.post(
        "/game/result?bet=50&prediction=1",
        json={
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjo5NDY2ODYwMDB9.CR_OzFi2WTQN7Y02eQXubB3rVRwyLv4JmxpkeV8vpas"  # noqa: E501
        },
    )

    assert response.status_code == 401
    assert response.json() == {
        "error_code": error_codes.EXPIRED_TOKEN,
        "detail": "The token has expired. Please login again.",
    }


def test_result_invalid_token_return_401(monkeypatch):
    def mock_get_result_raise_JWTError(**_):
        raise JWTError

    monkeypatch.setattr(
        "api.router.game.game.get_result",
        mock_get_result_raise_JWTError,
    )

    response = client.post(
        "/game/result?bet=50&prediction=1",
        json={
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjo5NDY2ODYwMDB9.CR_OzFi2WTQN7Y02eQXubB3rVRwyLv4JmxpkeV8vpas"  # noqa: E501
        },
    )

    assert response.status_code == 401
    assert response.json() == {
        "error_code": error_codes.INVALID_TOKEN,
        "detail": "The given token is invalid.",
    }


def test_result_no_such_game_returns_404(monkeypatch):
    def mock_get_result_raise_NoSuchGameException(**_):
        raise NoSuchGameException

    monkeypatch.setattr(
        "api.router.game.game.get_result",
        mock_get_result_raise_NoSuchGameException,
    )

    response = client.post(
        "/game/result?bet=50&prediction=1",
        json={
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjo5NDY2ODYwMDB9.CR_OzFi2WTQN7Y02eQXubB3rVRwyLv4JmxpkeV8vpas"  # noqa: E501
        },
    )

    assert response.status_code == 404
    assert response.json() == {
        "error_code": error_codes.NO_SUCH_GAME,
        "detail": "There is no game associated with this user.",
    }
