import os

import psycopg2
from dotenv import load_dotenv

from .encryption import Encryptor


class DatabaseConnection:
    def __init__(self):
        self.connection = self.connect_db()
        self.cursor = self.create_cursor()

    def add_new_player(self, username: str, password: str) -> None:
        """
        Adds a new player to the database

        :param username: The new player's username.
        :type username: str
        :param password: The new player's password.
        :type password: str
        """
        self.cursor.execute(
            "INSERT INTO users(username, password) VALUES (%s, %s);",
            (
                username,
                Encryptor.hash_password(password.encode()).decode(),
            ),
        )
        self.connection.commit()

    def connect_db(self):
        load_dotenv()

        connection = psycopg2.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host="localhost",
            port="5432",
            database="hilo",
        )
        return connection

    def create_cursor(self):
        cursor = self.connection.cursor()
        return cursor

    def retrieve_all_entries(self):
        self.cursor.execute("SELECT * FROM users;")
        return self.cursor.fetchall()

    def retrieve_last_entry(self):
        self.cursor.execute("SELECT * FROM users ORDER BY id DESC LIMIT 1")
        return self.cursor.fetchone()

    def retrieve_password_hash(self, username) -> bool:
        self.cursor.execute(
            "SELECT password FROM users WHERE username = (%s);", (username,)
        )

        return self.cursor.fetchone()[0]

    def is_returning_player(self, username: str) -> bool:
        self.cursor.execute(
            "SELECT * FROM users WHERE username = (%s);", (username,)
        )

        if not self.cursor.fetchone():
            return False

        return True
