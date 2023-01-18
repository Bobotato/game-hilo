from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_info():
    pass


def test_result():
    pass
