from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from api.database import get_db
from api.repository.errors import NoSuchUserException, UsernameTakenException
from api.router.user import schemas
from api.router.user.schemas import Token
from api.router.user.services import (
    create_token,
    register_user,
    verify_password,
)

router = APIRouter()


@router.post(
    "/user/authenticate", tags=["User Operations"], response_model=Token
)
def authenticate(request: schemas.Credentials, db: Session = Depends(get_db)):
    try:
        if not verify_password(credentials=request, db=db):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password does not match the given username.",
            )

    except NoSuchUserException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User does not exist.",
        )

    except InvalidRequestError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong.",
        )

    return {"access_token": create_token(credentials=request)}


@router.post("/user/register", tags=["User Operations"], response_model=Token)
def register(request: schemas.Credentials, db: Session = Depends(get_db)):
    try:
        register_user(
            credentials=request,
            db=db,
        )

    except UsernameTakenException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The username has already been taken.",
        )

    return {"access_token": create_token(credentials=request)}