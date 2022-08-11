import os

import psycopg2
from dotenv import load_dotenv


class DatabaseConnection:
    def __init__(self):
        self.connection = self.connect_db()
        self.cursor = self.create_cursor()

    def connect_db(self):
        load_dotenv()

        connection = psycopg2.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
        )

        connection.set_session(autocommit=True)

        return connection

    def create_cursor(self):
        cursor = self.connection.cursor()
        return cursor
