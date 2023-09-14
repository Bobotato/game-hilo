from fastapi import APIRouter, Depends, status, Response
from fastapi.responses import JSONResponse
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from api.database import get_db
from api.repository.errors import NoSuchUserException, UsernameTakenException
from api.router import error_codes
from api.router.user import schemas
from api.services.user.user import (
    create_access_token,
    register_user,
    verify_password,
)

router = APIRouter()


@router.post(
    "/user/authenticate",
    tags=["User Operations"],
    response_model=schemas.AuthenticateOut,
)
def authenticate(
    response: Response,
    credentials: schemas.AuthenticateIn,
    db: Session = Depends(get_db),
):
    try:
        if not verify_password(credentials=credentials, db=db):
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "error_code": error_codes.INVALID_CREDENTIALS,
                    "detail": "The credentials input were invalid.",
                },
            )

    except NoSuchUserException:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "error_code": error_codes.INVALID_CREDENTIALS,
                "detail": "The credentials input were invalid.",
            },
        )

    except InvalidRequestError:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error_code": error_codes.INVALID_REQUEST,
                "detail": "The request was invalid.",
            },
        )

    access_token = create_access_token(credentials=credentials)

    response.set_cookie("access_token", access_token)

    return {"access_token": access_token}


@router.post(
    "/user/register",
    tags=["User Operations"],
    response_model=schemas.RegisterOut,
)
def register(
    response: Response,
    credentials: schemas.RegisterIn,
    db: Session = Depends(get_db),
):
    try:
        register_user(
            credentials=credentials,
            db=db,
        )

    except UsernameTakenException:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "error_code": error_codes.USERNAME_TAKEN,
                "detail": "The username has already been taken.",
            },
        )

    access_token = create_access_token(credentials=credentials)

    response.set_cookie("access_token", access_token)

    return {"access_token": access_token}
