from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_authenticate(monkeypatch):
    def mock_get_user_by_username(*args, **kwargs):
        return 1

    monkeypatch.setattr(
        "api.router.user.user.get_user_by_username", mock_get_user_by_username
    )

    response = client.post(
        "/user/authenticate", json={"username": "test", "password": "test"}
    )

    assert response.status_code == 200
    assert (
        response.json()
        == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjo5NDY2ODYwMDB9.CR_OzFi2WTQN7Y02eQXubB3rVRwyLv4JmxpkeV8vpas"  # noqa: E501
    )


def test_authenticate_invalid_password(monkeypatch):
    def mock_get_user_by_username(*args, **kwargs):
        return 1

    def mock_verify_password_return_False(*args, **kwargs):
        return False

    monkeypatch.setattr(
        "api.router.user.user.get_user_by_username", mock_get_user_by_username
    )

    monkeypatch.setattr(
        "passlib.context.CryptContext.verify",
        mock_verify_password_return_False,
    )

    response = client.post(
        "/user/authenticate", json={"username": "test", "password": "test"}
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Password does not match the given username."
    }


def test_authenticate_username_does_not_exist(monkeypatch):
    def mock_get_user_by_username_return_None(*args, **kwargs):
        return None

    monkeypatch.setattr(
        "api.router.user.user.get_user_by_username",
        mock_get_user_by_username_return_None,
    )

    response = client.post(
        "/user/authenticate",
        json={"username": "doesnotexist", "password": "test"},
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "User does not exist."}
