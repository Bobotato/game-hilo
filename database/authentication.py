import bcrypt

from .repository import UserRepository


class UserManager:
    def __init__(self, username):
        self.repo = UserRepository()
        self.username = username

    def add_new_player(self, password: str) -> None:
        self.repo.add_new_entry(
            self.username, self.hash_password(password.encode()).decode()
        )
        self.repo.commit_update()

    def hash_password(self, encoded_password) -> bytes:
        return bcrypt.hashpw(encoded_password, bcrypt.gensalt())

    def is_existing_player(self) -> bool:
        if self.repo.retrieve_user(self.username) is None:
            return False
        else:
            return True

    def is_password_correct(self, password: str) -> bool:
        return bcrypt.checkpw(
            password.encode(),
            self.repo.retrieve_password_hash(self.username).encode(),
        )
