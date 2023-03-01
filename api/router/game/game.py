from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import get_db
from api.repository.errors import NoSuchGameException
from api.router.game import schemas
from api.services.game.game import get_info, get_result

router = APIRouter()


@router.post(
    "/game/info",
    summary="Gets the information for the current round.",
    tags=["Game Operations"],
    response_model=schemas.InfoOut,
)
def info(token: schemas.InfoIn, db: Session = Depends(get_db)):
    return get_info(token=token, db=db)


@router.post(
    "/game/result",
    summary="Gets the result of a game round.",
    tags=["Game Operations"],
    response_model=schemas.ResultOut,
)
def result(
    token: schemas.ResultIn,
    bet: int,
    prediction: int,
    db: Session = Depends(get_db),
):
    try:
        return get_result(bet=bet, prediction=prediction, token=token, db=db)

    except NoSuchGameException:
        raise HTTPException(
            status_code=400,
            detail="There is no game associated with this player.",
        )
