from fastapi import APIRouter, Depends, status, Response
from fastapi.responses import JSONResponse
from jose import ExpiredSignatureError, JWTError
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from api.database import get_db
from api.repository.errors import NoSuchUserException, UsernameTakenException
from api.router import error_codes
from api.router.user import schemas
from api.services.user.errors import TokenMismatchException
from api.services.user.user import (
    create_access_token,
    create_refresh_token,
    register_user,
    verify_password,
    update_token_pair,
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
    refresh_token = create_refresh_token(access_token)

    response.set_cookie("access_token", access_token)
    response.set_cookie(
        "refresh_token", refresh_token, secure=True, httponly=True
    )

    return {"access_token": access_token, "refresh_token": refresh_token}


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
    refresh_token = create_refresh_token(access_token)

    response.set_cookie("access_token", access_token)
    response.set_cookie(
        "refresh_token", refresh_token, secure=True, httponly=True
    )

    return {"access_token": access_token, "refresh_token": refresh_token}


@router.post(
    "/user/refresh_token",
    tags=["User Operations"],
    response_model=schemas.RefreshAccessTokenOut,
)
def refresh_token(
    response: Response, token_pair: schemas.RefreshAccessTokenIn
):
    try:
        new_access_token, new_refresh_token = update_token_pair(token_pair)

        response.set_cookie("access_token", new_access_token)
        response.set_cookie(
            "refresh_token", new_refresh_token, secure=True, httponly=True
        )

        return {
            "access_token": new_access_token,
            "refresh_token": new_refresh_token,
        }

    except ExpiredSignatureError:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "error_code": error_codes.EXPIRED_TOKEN,
                "detail": "The session has expired. Please login again.",
            },
        )

    except JWTError:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "error_code": error_codes.INVALID_TOKEN,
                "detail": "The given token is invalid.",
            },
        )

    except TokenMismatchException:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "error_code": error_codes.INVALID_TOKEN,
                "detail": "The refresh token is invalid.",
            },
        )


#    access_token = get_access_token_from_refresh_token(refresh_token)
#
#    update_refresh_token_with_access_token()
#
#    response.set_cookie("access_token", access_token)
#    response.set_cookie("refresh_token", refresh_token)

#    return {"access_token": access_token, "refresh_token": refresh_token}
