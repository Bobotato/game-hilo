import sys

import psycopg2

from database.connection import DatabaseConnection
from repository.errors import UserDoesNotExistException, UsernameTakenException
from repository.models.user import User


class UserRepository:
    def __init__(self):
        self.dbc = DatabaseConnection()

    def add_entry(self, user: User):
        """
        Adds a new user entry to the database

        :param user: The new player's user object.
        :type user: User
        """
        try:
            self.dbc.cursor.execute(
                "INSERT INTO users(username, password) VALUES (%s, %s);",
                (user.username, user.password_hash),
            )
        except psycopg2.errors.UniqueViolation:
            raise UsernameTakenException

        except psycopg2.Error:
            sys.exit("There was a fatal error with the database.")

    def get_entry(self, username: str) -> User:
        self.dbc.cursor.execute(
            "SELECT * FROM users WHERE username = (%s);",
            (username,),
        )
        try:
            _, username, password_hash = self.dbc.cursor.fetchone()
            return User(username, password_hash)

        except TypeError:
            raise UserDoesNotExistException
