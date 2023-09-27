from fastapi import APIRouter, Cookie, Depends, status
from fastapi.responses import JSONResponse
from jose import ExpiredSignatureError, JWTError
from sqlalchemy.orm import Session

from api.database import get_db
from api.repository.errors import NoSuchGameException
from api.router import error_codes
from api.router.game import schemas
from api.services.game.game import get_info, get_result, reset_game

router = APIRouter()


@router.post(
    "/game/info",
    summary="Gets the information for the current round.",
    tags=["Game Operations"],
    response_model=schemas.InfoOut,
)
def info(
    access_token: str = Cookie(None),
    db: Session = Depends(get_db),
):
    try:
        if access_token:
            return get_info(token=access_token, db=db)
        else:
            return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "error_code": error_codes.INVALID_TOKEN,
                "detail": "No token was supplied Please supply an access token.",
            },
        )

    except ExpiredSignatureError:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "error_code": error_codes.EXPIRED_TOKEN,
                "detail": "The token has expired. Please login again.",
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


@router.post(
    "/game/result",
    summary="Gets the result of a game round.",
    tags=["Game Operations"],
    response_model=schemas.ResultOut,
)
def result(
    bet: int,
    prediction: int,
    access_token: str = Cookie(None),
    db: Session = Depends(get_db),
):
    try:
        if access_token:
            return get_result(
                bet=bet, prediction=prediction, token=access_token, db=db
            )
        else:
            return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "error_code": error_codes.INVALID_TOKEN,
                "detail": "No token was supplied Please supply an access token.",
            },
        )

    except ExpiredSignatureError:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "error_code": error_codes.EXPIRED_TOKEN,
                "detail": "The token has expired. Please login again.",
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

    except NoSuchGameException:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "error_code": error_codes.NO_SUCH_GAME,
                "detail": "There is no game associated with this user.",
            },
        )


@router.post(
    "/game/reset", summary="Resets a player's game.", tags=["Game Operations"]
)
def reset(access_token: str = Cookie(None), db: Session = Depends(get_db)):
    try:
        reset_game(token=access_token, db=db)

    except ExpiredSignatureError:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "error_code": error_codes.EXPIRED_TOKEN,
                "detail": "The token has expired. Please login again.",
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
