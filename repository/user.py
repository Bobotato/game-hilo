import sys

import psycopg2

from repository.errors import NoSuchUserException, UsernameTakenException
from repository.models.user import User


def add_entry(cursor: psycopg2.extensions.cursor, user: User):
    """
    Adds a new user entry to the database
    :param user: The new player's user object.
    :type user: User
    """
    try:
        cursor.execute(
            "INSERT INTO users(username, password) VALUES (%s, %s);",
            (user.username, user.password_hash),
        )
    except psycopg2.errors.UniqueViolation:
        raise UsernameTakenException

    except psycopg2.Error:
        sys.exit("There was a fatal error with the database.")


def get_entry(cursor: psycopg2.extensions.cursor, username: str) -> User:
    cursor.execute(
        "SELECT * FROM users WHERE username = (%s);",
        (username,),
    )
    try:
        _, username, password_hash = cursor.fetchone()
        return User(username, password_hash)

    except TypeError:
        raise NoSuchUserException
