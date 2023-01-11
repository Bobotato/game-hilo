from datetime import datetime, timedelta

from fastapi import HTTPException
from jose import ExpiredSignatureError, JWTError, jwt

SECRETKEY = "0ffea62b0e68d011419a12e04afa69c3711d05035c8823627fdd603544f06a00"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20


def generate_token(data: dict) -> str:
    encode = data.copy()
    expiry = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    encode.update({"exp": expiry})
    return jwt.encode(encode, SECRETKEY, algorithm=ALGORITHM)


def decode_token(token: str):
    try:
        decoded_jwt = jwt.decode(token, SECRETKEY, algorithm=ALGORITHM)
        return decoded_jwt

    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token has expired.")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials.")
