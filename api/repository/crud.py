from sqlalchemy import update
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from api.models import User
from api.repository.errors import NoSuchUserException


class UserNotFoundException(Exception):
    pass


def get_game_by_username(username: str, db: Session) -> str:
    try:
        query = db.query(User).filter(User.username == username).first()
        return query.game

    except InvalidRequestError:
        raise InvalidRequestError("Filters are invalid")


def get_user_by_username(username: str, db: Session) -> User:
    try:
        user = db.query(User).filter(User.username == username).first()
        if user:
            return user

    except InvalidRequestError:
        raise InvalidRequestError("Filters are invalid")

    raise NoSuchUserException


def register_user(username: str, password_hash: str, db: Session) -> None:
    new_user = User(username=username, password_hash=password_hash)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)


def update_game(username: str, game: str, db: Session) -> None:
    db.execute(update(User).where(User.username == username).values(game=game))
    db.commit()
