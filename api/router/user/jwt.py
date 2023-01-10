from datetime import datetime, timedelta

from jose import jwt

SECRETKEY = "0ffea62b0e68d011419a12e04afa69c3711d05035c8823627fdd603544f06a00"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20


def generate_jwt(data: dict):
    encode = data.copy()
    expiry = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    encode.update({"exp": expiry})
    return jwt.encode(encode, SECRETKEY, algorithm=ALGORITHM)


def get_current_user(token: str):
    pass


def decode_token(token: str):
    decoded_jwt = jwt.decode(token, SECRETKEY, algorithm=ALGORITHM)
    return decoded_jwt
