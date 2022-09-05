import psycopg2
import pytest

from repository.errors import NoSuchUserException, UsernameTakenException
from repository.user import add_entry, get_entry


def mock_cursor_return_test(*args, **kwargs):
    class MockCursor:
        def execute(self, *args, **kwargs):
            return "test"

    return MockCursor


def mock_user():
    class MockUser:
        username = "test_username"
        password_hash = "test_password_hash"

    return MockUser


def test_add_entry_raise_UsernameTakenException(monkeypatch):
    def mock_cursor_raise_UniqueViolation():
        class MockCursorRaiseUniqueViolation:
            def execute(self, *args, **kwargs):
                raise psycopg2.errors.UniqueViolation

        return MockCursorRaiseUniqueViolation

    monkeypatch.setattr(
        "psycopg2.extensions.cursor", mock_cursor_raise_UniqueViolation
    )
    monkeypatch.setattr("repository.models.user.User", mock_user)

    with pytest.raises(UsernameTakenException):
        add_entry.__wrapped__(
            cursor=mock_cursor_raise_UniqueViolation(), user=mock_user()
        )


def test_add_entry_exit_on_Error(monkeypatch):
    def mock_cursor_raise_Error():
        class MockCursorRaiseError:
            def execute(self, *args, **kwargs):
                raise psycopg2.Error

        return MockCursorRaiseError

    monkeypatch.setattr("psycopg2.extensions.cursor", mock_cursor_raise_Error)
    monkeypatch.setattr("repository.models.user.User", mock_user)
    with pytest.raises(SystemExit):
        add_entry.__wrapped__(
            cursor=mock_cursor_raise_Error(), user=mock_user()
        )


def test_get_entry(monkeypatch):
    def mock_cursor_return_test():
        class MockCursorReturnTest:
            def execute(self, *args, **kwargs):
                return "test_execute"

            def fetchone(*args, **kwargs):
                return (1, "test_username", "test_password_hash")

        return MockCursorReturnTest

    monkeypatch.setattr("psycopg2.extensions.cursor", mock_cursor_return_test)
    monkeypatch.setattr("repository.models.user.User", mock_user)

    assertuser = get_entry.__wrapped__(
        cursor=mock_cursor_return_test(), username="test_username"
    )
    assert assertuser.username == "test_username"
    assert assertuser.password_hash == "test_password_hash"


def test_get_entry_raise_NoSuchUserException(monkeypatch):
    def mock_cursor_raise_TypeError():
        class MockCursorFetchoneRaiseTypeError:
            def execute(self, *args, **kwargs):
                return None

            def fetchone(self, *args, **kwargs):
                raise TypeError

        return MockCursorFetchoneRaiseTypeError

    monkeypatch.setattr(
        "psycopg2.extensions.cursor", mock_cursor_raise_TypeError
    )
    with pytest.raises(NoSuchUserException):
        get_entry.__wrapped__(
            cursor=mock_cursor_raise_TypeError(), username="test_username"
        )
