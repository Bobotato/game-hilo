from jose import ExpiredSignatureError, JWTError
from passlib.context import CryptContext
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from api.models import UserDetail
from api.repository.errors import NoSuchUserException, UsernameTakenException
from api.repository.user.user import UserRepository
from api.router.user import schemas
from api.services.user.errors import TokenMismatchException
from api.services.user.jwt import (
    decode_access_token,
    decode_refresh_token,
    generate_access_token,
    generate_refresh_token,
)

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(
    credentials: schemas.AuthenticateIn | schemas.RegisterIn,
) -> str:
    return generate_access_token(data={"sub": credentials.username})


def create_refresh_token(access_token: str) -> str:
    return generate_refresh_token(access_token)


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
            repo.get(
                target=UserDetail.password_hash, username=credentials.username
            ).password_hash,
        )

    except InvalidRequestError:
        raise InvalidRequestError

    except NoSuchUserException:
        raise NoSuchUserException


def verify_token_pair(token_pair: schemas.RefreshAccessTokenIn):
    try:
        payload = decode_refresh_token(token_pair.refresh_token)
        if token_pair.access_token == payload["access_token"]:
            return payload
        else:
            raise TokenMismatchException

    except ExpiredSignatureError:
        raise ExpiredSignatureError

    except JWTError:
        raise JWTError


def update_token_pair(token_pair: schemas.RefreshAccessTokenIn):
    payload = verify_token_pair(token_pair=token_pair)
    new_token_data = {
        "sub": decode_access_token(payload["access_token"])["sub"],
        "exp": payload["exp"],
    }
    new_token = generate_access_token(data=new_token_data)
    new_refresh_token = generate_refresh_token(
        access_token=new_token, exp=payload["exp"]
    )
    return new_token, new_refresh_token
