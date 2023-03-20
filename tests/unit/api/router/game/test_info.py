from fastapi.testclient import TestClient
from freezegun import freeze_time
from jose import ExpiredSignatureError, JWTError

from api.main import app
from api.router import error_codes

client = TestClient(app)


@freeze_time("2000-01-01")
def test_info(monkeypatch):
    def mock_get_info(**_):
        return {
            "player": {"name": "test", "credits": 100},
            "current_card": {"sort_index": 1, "rank": 1, "suit": 2},
        }

    monkeypatch.setattr("api.router.game.game.get_info", mock_get_info)

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


def test_info_expired_signature_returns_401(monkeypatch):
    def mock_get_info_raises_Expired_Signature_Error(**_):
        raise ExpiredSignatureError

    monkeypatch.setattr(
        "api.router.game.game.get_info",
        mock_get_info_raises_Expired_Signature_Error,
    )

    response = client.post(
        "/game/info",
        json={
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjo5NDY2ODYwMDB9.CR_OzFi2WTQN7Y02eQXubB3rVRwyLv4JmxpkeV8vpas"  # noqa: E501
        },
    )

    assert response.status_code == 401
    assert response.json() == {
        "error_code": error_codes.EXPIRED_TOKEN,
        "detail": "The token has expired. Please login again.",
    }


def test_info_JWT_error_returns_401(monkeypatch):
    def mock_get_info_raises_JWTError(**_):
        raise JWTError

    monkeypatch.setattr(
        "api.router.game.game.get_info",
        mock_get_info_raises_JWTError,
    )

    response = client.post(
        "/game/info",
        json={
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjo5NDY2ODYwMDB9.CR_OzFi2WTQN7Y02eQXubB3rVRwyLv4JmxpkeV8vpas"  # noqa: E501
        },
    )

    assert response.status_code == 401
    assert response.json() == {
        "error_code": error_codes.INVALID_TOKEN,
        "detail": "The given token is invalid.",
    }
