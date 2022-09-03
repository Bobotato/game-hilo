import bcrypt

from authentication.models.credentials import Credentials
from repository.errors import UsernameTakenException
from repository.models.user import User
from repository.user import add_entry, get_entry


def register(credentials: Credentials) -> None:
    try:
        add_entry(
            user=User(
                credentials.username,
                hash_password(credentials.password.encode()).decode(),
            ),
        )

    except UsernameTakenException:
        raise UsernameTakenException


def hash_password(encoded_password) -> bytes:
    return bcrypt.hashpw(encoded_password, bcrypt.gensalt())


def authenticate(credentials: Credentials) -> bool:
    return bcrypt.checkpw(
        credentials.password.encode(),
        get_entry(username=credentials.username).password_hash.encode(),
    )
