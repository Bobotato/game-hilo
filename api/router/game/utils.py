from fastapi import HTTPException
from sqlalchemy.orm import Session

from api.repository.crud import get_user_by_username
from api.repository.errors import NoSuchUserException
from api.router.user.jwt import decode_token
from api.router.user.schemas import Token


def get_user_from_token(token: Token, db: Session):
    try:
        user = get_user_by_username(
            username=decode_token(token=token.access_token)["sub"], db=db
        )

    except NoSuchUserException:
        raise HTTPException(status_code=400, detail="User does not exist.")

    return user
