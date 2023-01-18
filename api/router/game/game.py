from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import get_db
from api.repository.crud import get_user_by_username, update_game
from api.repository.errors import NoSuchUserException
from api.repository.pickler import pickle_object, unpickle_object
from api.router.game.schemas import Bet, Prediction, RoundResult
from api.router.user.jwt import decode_token
from api.router.user.schemas import Token
from hilo.game import Game

router = APIRouter()


@router.post(
    "/game/info",
    summary="Gets the information for the current round.",
    tags=["Game Operations"],
)
def info(token: Token, db: Session = Depends(get_db)):

    decoded_token = decode_token(token=token)
    username = decoded_token["sub"]
    # use username to get user row from db
    try:
        user = get_user_by_username(username=username, db=db)

    except NoSuchUserException:
        raise HTTPException(status_code=400, detail="User does not exist.")
    # if no game object create game object
    if not user.game:
        game = Game(username)
        # pickled_game = codecs.encode(pickle.dumps(game), "base64").decode()
        pickled_game = pickle_object(game)
        update_game(username=username, game=pickled_game, db=db)

    else:
        game = unpickle_object(user.game)
        # game = pickle.loads(codecs.decode((user.game).encode(), "base64"))
    # run game.start_round()
    roundinfo = game.start_round()
    return roundinfo

    # commit info to db
    # return info - currentcard
    # return roundinfo


@router.get(
    "/game/result",
    summary="Gets the result of a game round.",
    tags=["Game Operations"],
)
def result(
    token: Token,
    bet: Bet,
    prediction: Prediction,
    db: Session = Depends(get_db),
):
    decode_token(token)

    # game.compute_round_result(bet=bet, prediction=prediction)

    return RoundResult
