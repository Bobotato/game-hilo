from fastapi import FastAPI

from api import models
from api.database import engine
from api.router.game import game
from api.router.user import user

app = FastAPI()

app.include_router(user.router)
app.include_router(game.router)

models.Base.metadata.create_all(engine)
