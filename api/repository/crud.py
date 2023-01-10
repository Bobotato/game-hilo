from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from api.models import User


def get_user_by_username(username: str, db: Session) -> User:
    try:
        user = db.query(User).filter(User.username == username).first()
        return user

    except InvalidRequestError:
        raise InvalidRequestError("Filters are invalid")


def register_user(username: str, password_hash: str, db: Session) -> None:
    new_user = User(username=username, password_hash=password_hash)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
