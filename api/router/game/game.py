from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import get_db
from api.repository.errors import NoGameException, NoRoundInfoException
from api.router.game.schemas import RoundInfo, RoundResult
from api.router.game.services import get_info, get_result
from api.router.user.schemas import Token

router = APIRouter()


@router.post(
    "/game/info",
    summary="Gets the information for the current round.",
    tags=["Game Operations"],
    response_model=RoundInfo,
)
def info(token: Token, db: Session = Depends(get_db)):
    return get_info(token=token, db=db)


@router.post(
    "/game/result",
    summary="Gets the result of a game round.",
    tags=["Game Operations"],
    response_model=RoundResult,
)
def result(
    token: Token,
    bet: int,
    prediction: int,
    db: Session = Depends(get_db),
):
    try:
        return get_result(bet=bet, prediction=prediction, token=token, db=db)

    except NoGameException:
        raise HTTPException(
            status_code=400,
            detail="There is no game associated with this player.",
        )

    except NoRoundInfoException:
        raise HTTPException(
            status_code=403,
            detail="Round info does not exist, start a round first.",
        )
