from sqlalchemy.orm import Session

from api.models import User
from api.repository.errors import NoGameException, NoRoundInfoException
from api.repository.game.game import GameRepository
from api.router.game import schemas
from api.services.game.pickler import pickle_object, unpickle_object
from api.services.user.jwt import decode_token
from hilo.game import Game, Prediction
from hilo.models.roundinfo import RoundInfo
from hilo.models.roundresult import RoundResult


def get_game_object(username: str, repo: GameRepository) -> Game:
    pickled_game = repo.get(target=User.game, username=username)["game"]

    if pickled_game is None:
        raise NoGameException

    else:
        return unpickle_object(pickled_game)


def get_info(token: schemas.InfoIn, db: Session) -> RoundInfo:
    repo = GameRepository.create(db)

    username = get_username_from_token(token=token)

    try:
        game = get_game_object(username=username, repo=repo)

    except NoGameException:
        game = Game(name=username)

    round_info = game.start_round()

    update_game(username=username, game=game, repo=repo)
    update_round_info(username=username, round_info=round_info, repo=repo)

    return round_info


def get_result(
    bet: int, prediction: int, token: schemas.ResultIn, db: Session
) -> RoundResult:
    repo = GameRepository.create(db)

    username = get_username_from_token(token=token)

    try:
        game = get_game_object(username=username, repo=repo)

    except NoGameException:
        raise NoGameException

    try:
        get_round_info_object(username=username, repo=repo)

    except NoRoundInfoException:
        raise NoRoundInfoException

    round_result = game.compute_round_result(
        bet=bet, prediction=Prediction(int(prediction))
    )

    update_game(username=username, game=game, repo=repo)

    return round_result


def get_round_info_object(username: str, repo: GameRepository) -> RoundInfo:
    pickled_round_info = repo.get(target=User.round_info, username=username)[
        "round_info"
    ]

    if pickled_round_info is None:
        raise NoRoundInfoException

    else:
        return unpickle_object(pickled_round_info)


def get_username_from_token(token: schemas.InfoIn | schemas.ResultIn) -> str:
    return decode_token(token=token.access_token)["sub"]


def update_game(username: str, game: Game, repo: GameRepository) -> None:
    repo.patch(
        target=User.username,
        search_term=username,
        game=pickle_object(game),
    )


def update_round_info(
    username: str, round_info: RoundInfo, repo: GameRepository
) -> None:
    repo.patch(
        target=User.username,
        search_term=username,
        round_info=pickle_object(round_info),
    )
