from sqlalchemy.orm import Session

from api.repository.crud import (
    get_game_by_username,
    get_round_info_by_username,
    update_game,
    update_round_info,
)
from api.repository.errors import NoGameException, NoRoundInfoException
from api.router.game.pickler import pickle_object, unpickle_object
from api.router.user.jwt import decode_token
from api.router.user.schemas import Token
from hilo.game import Game, Prediction


def get_username_from_token(token: Token):
    return decode_token(token=token.access_token)["sub"]


def get_game_object(username: str, db: Session):
    try:
        return unpickle_object(get_game_by_username(username=username, db=db))

    except NoGameException:
        raise NoGameException


def get_round_info_object(username: str, db: Session):
    try:
        return unpickle_object(
            get_round_info_by_username(username=username, db=db)
        )

    except NoRoundInfoException:
        raise NoRoundInfoException


def get_info(token: Token, db: Session):
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


def get_result(bet: int, prediction: int, token: Token, db: Session):
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
