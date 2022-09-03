import psycopg2
import pytest

from database.connection import DatabaseConnection


class MockConnection:
    def __init__(self):
        self.closed = "connection open"
        self.session = "no autocommit"

    def close(self, **kwargs):
        self.closed = "connection closed"

    def cursor(self, **kwargs):
        return "cursor opened"

    def set_session(self, **kwargs):
        self.session = "session autocommit enabled"


def open_connection(**kwargs):
    return MockConnection()


def test_DatabaseConnection_init(monkeypatch):
    def mock_psycopg2(**kwargs):
        class MockDatabaseConnection:
            def connect_db(self):
                return "connected_db"

            def create_cursor(self):
                return "created cursor"

        return MockDatabaseConnection()

    monkeypatch.setattr(psycopg2, "connect", open_connection)

    conn = DatabaseConnection()
    assert isinstance(conn.connection, MockConnection)
    assert conn.connection.closed == "connection open"


def test_bind_connection(monkeypatch):
    monkeypatch.setattr(DatabaseConnection, "connect_db", lambda: None)
    monkeypatch.setattr(DatabaseConnection, "create_cursor", lambda: "cursor")
    monkeypatch.setattr(DatabaseConnection, "close_connection", lambda: None)

    @DatabaseConnection.bind_connection
    def test_function(cursor, *args, **kwargs):
        assert cursor == "cursor"
        return "return"

    assert test_function() == "return"


def test_connect_db(monkeypatch):
    monkeypatch.setattr(psycopg2, "connect", open_connection)

    conn = DatabaseConnection()
    assert isinstance(conn.connection, MockConnection)
    assert conn.connection.session == "session autocommit enabled"


def test_connect_db_exits_on_raising_OperationalError(monkeypatch):
    def raise_OperationalError(**kwargs):
        raise psycopg2.errors.OperationalError

    monkeypatch.setattr(psycopg2, "connect", raise_OperationalError)
    with pytest.raises(SystemExit):
        DatabaseConnection()


def test_connect_db_exits_on_raising_Error(monkeypatch):
    def raise_Error(**kwargs):
        raise psycopg2.Error

    monkeypatch.setattr(psycopg2, "connect", raise_Error)
    with pytest.raises(SystemExit):
        DatabaseConnection()


def test_close_connection(monkeypatch):
    monkeypatch.setattr(psycopg2, "connect", open_connection)
    conn = DatabaseConnection()
    assert conn.connection.closed == "connection open"
    conn.close_connection()
    assert conn.connection.closed == "connection closed"
