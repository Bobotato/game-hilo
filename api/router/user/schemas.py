from pydantic import BaseModel


class AuthenticateIn(BaseModel):
    username: str
    password: str


class AuthenticateOut(BaseModel):
    access_token: str


class RegisterIn(BaseModel):
    username: str
    password: str


class RegisterOut(BaseModel):
    access_token: str
