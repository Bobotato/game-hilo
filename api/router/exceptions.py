from fastapi import Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import InvalidRequestError

from api.repository.errors import (
    ExpiredTokenException,
    InvalidCredentialsException,
    InvalidTokenException,
    NoSuchGameException,
    UsernameTakenException,
)
from api.router import error_codes


def expired_token_exception_handler(
    request: Request, exc: ExpiredTokenException
):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content=error_codes.EXPIRED_TOKEN,
    )


def invalid_credentials_exception_handler(
    request: Request, exc: InvalidCredentialsException
):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content=error_codes.INVALID_CREDENTIALS,
    )


def invalid_filters_exception_handler(
    request: Request, exc: InvalidRequestError
):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=error_codes.INVALID_REQUEST,
    )


def invalid_token_exception_handler(
    request: Request, exc: InvalidTokenException
):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content=error_codes.INVALID_TOKEN,
    )


def no_such_game_exception_handler(request: Request, exc: NoSuchGameException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content=error_codes.NO_SUCH_GAME
    )


def username_taken_exception_handler(
    request: Request, exc: UsernameTakenException
):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content=error_codes.USERNAME_TAKEN,
    )
