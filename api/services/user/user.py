from passlib.context import CryptContext
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from api.repository.crud import (
    add_user,
    get_password_hash_by_username,
    get_user_by_username,
)
from api.repository.errors import NoSuchUserException, UsernameTakenException
from api.router.user import schemas
from api.services.user.jwt import generate_token

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_token(
    credentials: schemas.AuthenticateIn | schemas.RegisterIn,
) -> str:
    return generate_token(data={"sub": credentials.username})


def register_user(credentials: schemas.RegisterIn, db: Session) -> None:
    try:
        if get_user_by_username(username=credentials.username, db=db):
            raise UsernameTakenException

    except NoSuchUserException:
        add_user(
            credentials.username,
            password_context.hash(credentials.password),
            db=db,
        )


def verify_password(credentials: schemas.AuthenticateIn, db: Session) -> bool:
    try:
        return password_context.verify(
            credentials.password,
            get_password_hash_by_username(
                username=credentials.username, db=db
            ),
        )

    except InvalidRequestError:
        raise InvalidRequestError

    except NoSuchUserException:
        raise NoSuchUserException
