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
                hash_password(credentials.password),
            ),
        )

    except UsernameTakenException:
        raise UsernameTakenException


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode("latin-1")


def authenticate(credentials: Credentials) -> bool:
    return bcrypt.checkpw(
        credentials.password.encode(),
        get_entry(username=credentials.username).password_hash.encode(
            "latin-1"
        ),
    )
