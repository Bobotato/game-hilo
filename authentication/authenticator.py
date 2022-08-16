import bcrypt
import psycopg2

from database.connection import DatabaseConnection
from repository.errors import UsernameTakenException
from repository.models.user import User
from repository.user import add_entry, get_entry


@DatabaseConnection.bind_connection
def register(
    cursor: psycopg2.extensions.cursor, username: str, password: str
) -> None:
    try:
        add_entry(
            cursor,
            User(username, hash_password(password.encode()).decode()),
        )

    except UsernameTakenException:
        raise UsernameTakenException


def hash_password(encoded_password) -> bytes:
    return bcrypt.hashpw(encoded_password, bcrypt.gensalt())


@DatabaseConnection.bind_connection
def authenticate(
    cursor: psycopg2.extensions.cursor, username: str, password: str
) -> bool:
    return bcrypt.checkpw(
        password.encode(), get_entry(cursor, username).password_hash.encode()
    )
