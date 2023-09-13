import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from jose import ExpiredSignatureError, JWTError, jwt

from api.services.user.errors import JWTEnvNotFoundException

load_dotenv()


def generate_access_token(data: dict) -> str:
    try:
        encode = data.copy()
        expiry = datetime.utcnow() + timedelta(
            minutes=float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
        )
        encode.update({"exp": expiry})

        return jwt.encode(
            encode,
            os.getenv("JWT_SECRET_KEY"),
            algorithm=os.getenv("JWT_ALGORITHM"),
        )

    except KeyError:
        raise JWTEnvNotFoundException


def generate_refresh_token(
    access_token: str,
    exp: int = datetime.utcnow()
    + timedelta(minutes=float(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES"))),
) -> str:
    try:
        encode = {"access_token": access_token}
        encode.update({"exp": exp})

        return jwt.encode(
            encode,
            os.getenv("JWT_REFRESH_SECRET_KEY"),
            algorithm=os.getenv("JWT_ALGORITHM"),
        )

    except KeyError:
        raise JWTEnvNotFoundException


def decode_access_token(access_token: str) -> dict:
    try:
        decoded_jwt = jwt.decode(
            access_token,
            os.getenv("JWT_SECRET_KEY"),
            algorithms=[os.getenv("JWT_ALGORITHM")],
        )
        return decoded_jwt

    except ExpiredSignatureError:
        raise ExpiredSignatureError

    except JWTError:
        raise JWTError


def decode_refresh_token(refresh_token: str) -> dict:
    try:
        decoded_jwt = jwt.decode(
            refresh_token,
            os.getenv("JWT_REFRESH_SECRET_KEY"),
            algorithms=[os.getenv("JWT_ALGORITHM")],
        )
        return decoded_jwt

    except ExpiredSignatureError:
        raise ExpiredSignatureError

    except JWTError:
        raise JWTError
