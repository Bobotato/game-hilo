import pytest
from freezegun import freeze_time
from jose import ExpiredSignatureError, JWTError

from api.services.user.jwt import decode_access_token, generate_access_token

invalid_token = "nonsense"

test_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZXhwIjo5NDY2ODYwMDB9.CR_OzFi2WTQN7Y02eQXubB3rVRwyLv4JmxpkeV8vpas"  # noqa: E501


@freeze_time("2000-01-01")
def test_generate_token():
    data = {"sub": "test"}

    assert generate_access_token(data=data) == test_token


@freeze_time("1990-01-01")
def test_decode_token():
    assert decode_access_token(test_token) == {"exp": 946686000, "sub": "test"}


def test_decode_token_raise_ExpiredSignatureError():
    with pytest.raises(ExpiredSignatureError):
        decode_access_token(test_token)


def test_decode_token_raise_JWTError():
    with pytest.raises(JWTError):
        decode_access_token(invalid_token)
