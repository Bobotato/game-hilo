from sqlalchemy.orm import Session

from api.models import GameState
from api.repository.errors import GenericException, NoSuchGameException
from api.repository.game.game import GameRepository
from api.repository.pickler import pickle_object, unpickle_object
from api.router.game import schemas
from api.services.user.jwt import decode_token
from hilo.game import Game, Prediction
from hilo.models.roundresult import RoundResult


def create_game_state(username: str, repo: GameRepository) -> None:
    repo.add(user=GameState(username=username))


def get_game_object(username: str, repo: GameRepository) -> Game:
    try:
        pickled_game = repo.get(target=GameState.game, username=username)[
            "game"
        ]

    except GenericException:
        raise NoSuchGameException

    return unpickle_object(pickled_game)


def get_info(token: schemas.InfoIn, db: Session):
    repo = GameRepository.create(db)

    username = get_username_from_token(token=token)

    try:
        game = get_game_object(username=username, repo=repo)

    except NoSuchGameException:
        create_game_state(username=username, repo=repo)
        game = Game(name=username)

    round_info = game.start_round()

    update_game(username=username, game=game, repo=repo)

    return round_info


def get_result(
    bet: int, prediction: int, token: schemas.ResultIn, db: Session
) -> RoundResult:

    repo = GameRepository.create(db)

    username = get_username_from_token(token=token)

    try:
        game = get_game_object(username=username, repo=repo)

    except GenericException:
        raise NoSuchGameException

    round_result = game.compute_round_result(
        bet=bet, prediction=Prediction(int(prediction))
    )

    update_game(username=username, game=game, repo=repo)

    return round_result


def get_username_from_token(token: schemas.InfoIn | schemas.ResultIn) -> str:
    return decode_token(token=token.access_token)["sub"]


def update_game(username: str, game: Game, repo: GameRepository) -> None:
    repo.patch(
        target=GameState.username,
        search_term=username,
        game=pickle_object(game),
    )
