import bcrypt

from repository.errors import UsernameTakenException
from repository.models.user import User
from repository.user import UserRepository


class UserManager:
    def __init__(self):
        self.repo = UserRepository()

    def add_new_player(self, username: str, password: str) -> None:
        try:
            self.repo.add_entry(
                User(username, self.hash_password(password.encode()).decode())
            )
        except UsernameTakenException:
            raise UsernameTakenException

    def hash_password(self, encoded_password) -> bytes:
        return bcrypt.hashpw(encoded_password, bcrypt.gensalt())

    def is_password_correct(self, username: str, password: str) -> bool:
        return bcrypt.checkpw(
            password.encode(),
            self.repo.get_entry(username).password_hash.encode(),
        )
