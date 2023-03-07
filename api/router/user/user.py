from fastapi import APIRouter, Depends
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from api.database import get_db
from api.repository.errors import (
    InvalidCredentialsException,
    NoSuchUserException,
    UsernameTakenException,
)
from api.router.user import schemas
from api.services.user.user import create_token, register_user, verify_password

router = APIRouter()


@router.post(
    "/user/authenticate",
    tags=["User Operations"],
    response_model=schemas.AuthenticateOut,
)
def authenticate(
    credentials: schemas.AuthenticateIn, db: Session = Depends(get_db)
):
    try:
        if not verify_password(credentials=credentials, db=db):
            raise InvalidCredentialsException

    except NoSuchUserException:
        raise InvalidCredentialsException

    except InvalidRequestError:
        raise InvalidRequestError

    return {"access_token": create_token(credentials=credentials)}


@router.post(
    "/user/register",
    tags=["User Operations"],
    response_model=schemas.RegisterOut,
)
def register(credentials: schemas.RegisterIn, db: Session = Depends(get_db)):
    try:
        register_user(
            credentials=credentials,
            db=db,
        )

    except UsernameTakenException:
        raise UsernameTakenException

    return {"access_token": create_token(credentials=credentials)}
