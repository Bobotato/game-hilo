from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import get_db
from api.repository.crud import update_game, update_round_info
from api.repository.pickler import pickle_object, unpickle_object
from api.router.game.schemas import RoundInfo, RoundResult
from api.router.game.utils import get_user_from_token
from api.router.user.schemas import Token
from hilo.game import Game, Prediction

router = APIRouter()


@router.post(
    "/game/info",
    summary="Gets the information for the current round.",
    tags=["Game Operations"],
    response_model=RoundInfo,
)
def info(token: Token, db: Session = Depends(get_db)):

    user = get_user_from_token(token=token, db=db)

    if not user.game:
        game = Game(name=user.username)
        pickled_game = pickle_object(object=game)
        update_game(username=user.username, value=pickled_game, db=db)

    else:
        game = unpickle_object(pickled_object=user.game)

    roundinfo = game.start_round()

    update_round_info(
        username=user.username,
        value=pickle_object(object=roundinfo),
        db=db,
    )
    update_game(
        username=user.username, value=pickle_object(object=game), db=db
    )

    return roundinfo


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
    user = get_user_from_token(token=token, db=db)

    if not user.game:
        raise HTTPException(
            status_code=400,
            detail="There is no game associated with this player.",
        )

    if not user.round_info:
        raise HTTPException(
            status_code=403,
            detail="Round info does not exist, start a round first.",
        )

    game = unpickle_object(pickled_object=user.game)

    roundresult = game.compute_round_result(
        bet=bet, prediction=Prediction(int(prediction))
    )

    update_game(
        username=user.username, value=pickle_object(object=game), db=db
    )

    return roundresult
