from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db
from api.router.game.schemas import RoundInfo, RoundResult
from api.router.user.user.schemas import Token

router = APIRouter()


@router.get("/game/info", tags=["Game Operations"])
def info(request: Token, db: Session = Depends(get_db)):
    return RoundInfo


@router.get("/game/result", tags=["Game Operations"])
def result(request: Token, db: Session = Depends(get_db)):
    return RoundResult
