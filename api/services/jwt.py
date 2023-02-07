import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from fastapi import HTTPException
from jose import ExpiredSignatureError, JWTError, jwt

load_dotenv()
ACCESS_TOKEN_EXPIRE_MINUTES = 20


def generate_token(data: dict) -> str:
    encode = data.copy()
    expiry = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    encode.update({"exp": expiry})
    return jwt.encode(
        encode,
        os.getenv("JWT_SECRET_KEY"),
        algorithm=os.getenv("JWT_ALGORITHM"),
    )


def decode_token(token: str) -> dict:
    try:
        decoded_jwt = jwt.decode(
            token,
            os.getenv("JWT_SECRET_KEY"),
            algorithms=[os.getenv("JWT_ALGORITHM")],
        )
        return decoded_jwt

    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token has expired.")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials.")
