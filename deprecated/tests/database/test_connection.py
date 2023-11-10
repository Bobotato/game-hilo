import psycopg2
import pytest
from database.connection import DatabaseConnection


class MockConnection:
    def __init__(self):
        self.closed = "connection open"
        self.session = "no autocommit"

    def close(self, **_):
        self.closed = "connection closed"

    def cursor(self, **_):
        return "cursor opened"

    def set_session(self, **_):
        self.session = "session autocommit enabled"


def open_connection(**_):
    return MockConnection()


def test_DatabaseConnection_init(monkeypatch):
    monkeypatch.setattr(psycopg2, "connect", open_connection)

    conn = DatabaseConnection()
    assert isinstance(conn.connection, MockConnection)
    assert conn.connection.closed == "connection open"


def test_bind_connection(monkeypatch):
    monkeypatch.setattr(DatabaseConnection, "connect_db", lambda *_: None)
    monkeypatch.setattr(DatabaseConnection, "create_cursor", lambda *_: "cursor")
    monkeypatch.setattr(DatabaseConnection, "close_connection", lambda *_: None)

    @DatabaseConnection.bind_connection
    def test_function(cursor=None, *_):
        assert cursor == "cursor"
        return "return"

    assert test_function() == "return"


def test_connect_db(monkeypatch):
    monkeypatch.setattr(psycopg2, "connect", open_connection)

    conn = DatabaseConnection()
    assert isinstance(conn.connection, MockConnection)
    assert conn.connection.session == "session autocommit enabled"


def test_connect_db_exits_on_raising_OperationalError(monkeypatch):
    def raise_OperationalError(**_):
        raise psycopg2.errors.OperationalError  # pyright: ignore [reportGeneralTypeIssues] # noqa: E501

    monkeypatch.setattr(psycopg2, "connect", raise_OperationalError)
    with pytest.raises(SystemExit):
        DatabaseConnection()


def test_connect_db_exits_on_raising_Error(monkeypatch):
    def raise_Error(**_):
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
