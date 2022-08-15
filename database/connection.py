import os
import sys

import psycopg2
from dotenv import load_dotenv


class DatabaseConnection:
    def __init__(self):
        self.connection: psycopg2.extensions.connection = self.connect_db()
        self.cursor: psycopg2.extensions.cursor = self.create_cursor()

    def connect_db(self) -> psycopg2.extensions.connection:
        load_dotenv()

        try:
            connection = psycopg2.connect(
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_NAME"),
            )

        except psycopg2.errors.OperationalError:
            sys.exit("There was an issue connecting to the database.")

        except psycopg2.Error:
            sys.exit("There was a fatal error with the database.")

        connection.set_session(autocommit=True)

        return connection

    def create_cursor(self) -> psycopg2.extensions.cursor:
        cursor = self.connection.cursor()
        return cursor

    def close_connection(self) -> None:
        self.connection.cursor()
        self.connection.close()
