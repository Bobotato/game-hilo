from fastapi import HTTPException
from sqlalchemy.orm import Session

from api.repository.crud import get_user_by_username
from api.repository.errors import NoSuchUserException
from api.router.user.jwt import decode_token
from api.router.user.schemas import Token


def get_user_from_token(token: Token, db: Session):
    decoded_token = decode_token(token=token.access_token)
    username = decoded_token["sub"]
    try:
        user = get_user_by_username(username=username, db=db)

    except NoSuchUserException:
        raise HTTPException(status_code=400, detail="User does not exist.")

    return user
