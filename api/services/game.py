from sqlalchemy.orm import Session

from api.repository.crud import (
    get_game_by_username,
    get_round_info_by_username,
    update_game,
    update_round_info,
)
from api.repository.errors import NoGameException, NoRoundInfoException
from api.router.game import schemas
from api.router.game.pickler import pickle_object, unpickle_object
from api.router.user.jwt import decode_token
from hilo.game import Game, Prediction
from hilo.models.roundinfo import RoundInfo
from hilo.models.roundresult import RoundResult


def get_game_object(username: str, db: Session) -> Game:
    try:
        return unpickle_object(get_game_by_username(username=username, db=db))

    except NoGameException:
        raise NoGameException


def get_info(token: schemas.InfoIn, db: Session) -> RoundInfo:
    username = get_username_from_token(token=token)

    try:
        game = get_game_object(username=username, db=db)

    except NoGameException:
        game = Game(name=username)

    round_info = game.start_round()

    update_game(username=username, game=pickle_object(game), db=db)
    update_round_info(
        username=username, round_info=pickle_object(round_info), db=db
    )

    return round_info


def get_result(
    bet: int, prediction: int, token: schemas.ResultIn, db: Session
) -> RoundResult:
    username = get_username_from_token(token=token)

    try:
        game = get_game_object(username=username, db=db)

    except NoGameException:
        raise NoGameException

    try:
        get_round_info_object(username=username, db=db)

    except NoRoundInfoException:
        raise NoRoundInfoException

    round_result = game.compute_round_result(
        bet=bet, prediction=Prediction(int(prediction))
    )

    update_game(username=username, game=pickle_object(game), db=db)

    return round_result


def get_round_info_object(username: str, db: Session) -> RoundInfo:
    try:
        return unpickle_object(
            get_round_info_by_username(username=username, db=db)
        )

    except NoRoundInfoException:
        raise NoRoundInfoException


def get_username_from_token(token: schemas.InfoIn | schemas.ResultIn) -> str:
    return decode_token(token=token.access_token)["sub"]
