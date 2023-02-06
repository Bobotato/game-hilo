from sqlalchemy import update
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from api.models import User
from api.repository.errors import (
    NoGameException,
    NoRoundInfoException,
    NoSuchUserException,
)


def get_user_by_username(username: str, db: Session) -> User:
    try:
        user = db.query(User).filter(User.username == username).first()
        if user:
            return user

    except InvalidRequestError:
        raise InvalidRequestError("Filters are invalid")

    raise NoSuchUserException


def get_game_by_username(username: str, db: Session) -> str:
    try:
        game = db.query(User.game).filter_by(username=username).scalar()
        if game:
            return game

    except InvalidRequestError:
        raise InvalidRequestError("Filters are invalid")

    raise NoGameException


def get_round_info_by_username(username: str, db: Session) -> str:
    try:
        round_info = (
            db.query(User.round_info).filter_by(username=username).scalar()
        )
        if round_info:
            return round_info

    except InvalidRequestError:
        raise InvalidRequestError("Filters are invalid")

    raise NoRoundInfoException


def get_password_hash_by_username(username: str, db: Session) -> str:
    try:
        hash = (
            db.query(User.password_hash).filter_by(username=username).scalar()
        )
        if hash:
            return hash

    except InvalidRequestError:
        raise InvalidRequestError("Filters are invalid")

    raise NoSuchUserException


def add_user(username: str, password_hash: str, db: Session) -> None:
    new_user = User(username=username, password_hash=password_hash)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)


def update_game(username: str, game: str, db: Session) -> None:
    db.execute(update(User).where(User.username == username).values(game=game))
    db.commit()


def update_round_info(username: str, round_info: str, db: Session) -> None:
    db.execute(
        update(User)
        .where(User.username == username)
        .values(round_info=round_info)
    )
    db.commit()
