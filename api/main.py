from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import models
from api.database import engine
from api.router.game import game
from api.router.user import user

app = FastAPI()

app.include_router(user.router)
app.include_router(game.router)

origins = ["http://localhost:8080", "http://localhost:5173"]

app = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)
