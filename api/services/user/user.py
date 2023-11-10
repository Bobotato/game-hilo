from passlib.context import CryptContext
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from api.models import UserDetail
from api.repository.errors import NoSuchUserException, UsernameTakenException
from api.repository.user.user import UserRepository
from api.router.user import schemas
from api.services.user.jwt import generate_access_token

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(
    credentials: schemas.AuthenticateIn | schemas.RegisterIn,
) -> str:
    return generate_access_token(data={"username": credentials.username})


def register_user(credentials: schemas.RegisterIn, db: Session) -> None:
    repo = UserRepository.create(db)

    try:
        if repo.get(target=UserDetail.username, username=credentials.username):
            raise UsernameTakenException

    except NoSuchUserException:
        repo.add(
            UserDetail(
                username=credentials.username,
                password_hash=password_context.hash(credentials.password),
            )
        )


def verify_password(credentials: schemas.AuthenticateIn, db: Session) -> bool:
    repo = UserRepository.create(db)

    try:
        return password_context.verify(
            credentials.password,
            repo.get(target=UserDetail.password_hash, username=credentials.username).password_hash,
        )

    except InvalidRequestError:
        raise InvalidRequestError

    except NoSuchUserException:
        raise NoSuchUserException
