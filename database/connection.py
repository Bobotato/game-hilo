import hashlib

import psycopg2


class DatabaseConnection:
    def __init__(self, password):
        self.connection = self.connect_db(password)
        self.cursor = self.create_cursor()

    def add_new_player(self, username: str, password: str) -> None:
        self.cursor.execute(
            "INSERT INTO users(username, password) VALUES (%s, %s);",
            (username, password),
        )
        self.connection.commit()

    def connect_db(self, password):
        connection = psycopg2.connect(
            user="hilo",
            password=password,
            host="localhost",
            port="5432",
            database="hilo",
        )
        return connection

    def create_cursor(self):
        cursor = self.connection.cursor()
        return cursor

    def hash_password(self, password):
        return str(hashlib.sha256(password).hexdigest())

    def is_password_correct(self, username, password) -> bool:
        self.cursor.execute(
            "SELECT password FROM users WHERE username = (%s);", (username,)
        )

        return password == self.cursor.fetchone()[0]

    def is_returning_player(self, username: str) -> bool:
        self.cursor.execute(
            "SELECT * FROM users WHERE username = (%s);", (username,)
        )

        if not self.cursor.fetchone():
            return False

        return True
