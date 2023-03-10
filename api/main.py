from fastapi import FastAPI

from api import models
from api.database import engine
from api.router.game import game
from api.router.user import user

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(user.router)
app.include_router(game.router)


@app.get("/ping", tags=["Testing Operations"])
def ping():
    return {"msg": "Pong"}
