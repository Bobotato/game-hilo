from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from api.database import get_db
from api.repository.crud import get_user_by_username, register_user
from api.repository.errors import NoSuchUserException
from api.router.user import schemas
from api.router.user.jwt import generate_token
from api.router.user.schemas import Token

router = APIRouter()

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post(
    "/user/authenticate", tags=["User Operations"], response_model=Token
)
def authenticate(request: schemas.Credentials, db: Session = Depends(get_db)):
    try:
        user = get_user_by_username(username=request.username, db=db)

    except NoSuchUserException:
        raise HTTPException(status_code=400, detail="User does not exist.")

    if not password_context.verify(request.password, user.password_hash):
        raise HTTPException(
            status_code=400,
            detail="Password does not match the given username.",
        )

    access_token = generate_token(data={"sub": user.username})
    return {"access_token": access_token}


@router.post("/user/register", tags=["User Operations"], response_model=Token)
def register(request: schemas.Credentials, db: Session = Depends(get_db)):
    if get_user_by_username(username=request.username, db=db):
        raise HTTPException(
            status_code=409,
            detail="Account with the given username already exists",
        )

    register_user(
        username=request.username,
        password_hash=password_context.hash(request.password),
        db=db,
    )

    access_token = generate_token(data={"sub": request.username})
    return {"access_token": access_token}
