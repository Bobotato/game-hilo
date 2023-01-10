from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db
from api.router.game.schemas import RoundInfo, RoundResult

router = APIRouter()


@router.get("/game/info", tags=["Game Operations"])
def info(db: Session = Depends(get_db)):
    return RoundInfo


@router.get("/game/result", tags=["Game Operations"])
def result(db: Session = Depends(get_db)):
    return RoundResult
