from pydantic import BaseModel


class AuthenticateIn(BaseModel):
    username: str
    password: str


class AuthenticateOut(BaseModel):
    access_token: str

    class Config:
        orm_mode = True


class RegisterIn(BaseModel):
    username: str
    password: str


class RegisterOut(BaseModel):
    access_token: str
