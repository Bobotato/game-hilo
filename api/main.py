from fastapi import FastAPI

from api import models
from api.database import engine
from api.repository.errors import (
    ExpiredTokenException,
    InvalidCredentialsException,
    InvalidTokenException,
    NoSuchGameException,
    UsernameTakenException,
)
from api.router.exceptions import (
    expired_token_exception_handler,
    invalid_credentials_exception_handler,
    invalid_token_exception_handler,
    no_such_game_exception_handler,
    username_taken_exception_handler,
)
from api.router.game import game
from api.router.user import user

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(user.router)
app.include_router(game.router)

app.add_exception_handler(
    ExpiredTokenException, expired_token_exception_handler
)
app.add_exception_handler(
    InvalidCredentialsException, invalid_credentials_exception_handler
)
app.add_exception_handler(
    InvalidTokenException, invalid_token_exception_handler
)
app.add_exception_handler(NoSuchGameException, no_such_game_exception_handler)
app.add_exception_handler(
    UsernameTakenException, username_taken_exception_handler
)


@app.get("/ping", tags=["Testing Operations"])
def ping():
    return {"msg": "Pong"}
