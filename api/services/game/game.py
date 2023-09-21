from sqlalchemy.orm import Session

from api.models import GameState
from api.repository.errors import NoSuchGameException
from api.repository.game.game import GameRepository
from api.router.game import schemas
from api.services.user.jwt import decode_access_token
from hilo.game import Game, Prediction
from hilo.models.roundresult import RoundResult


def create_game_state(username: str, repo: GameRepository) -> None:
    repo.add(user=GameState(username=username))


def get_game_object(username: str, repo: GameRepository) -> Game:
    try:
        return repo.get(target=GameState.game, username=username)

    except NoSuchGameException:
        raise NoSuchGameException


def get_info(token: str, db: Session):
    repo = GameRepository.create(db)

    username = decode_access_token(access_token=token)["username"]

    try:
        game = get_game_object(username=username, repo=repo)

    except NoSuchGameException:
        create_game_state(username=username, repo=repo)
        game = Game(name=username)

    round_info = game.start_round()

    update_game(username=username, game=game, repo=repo)

    return round_info


def get_result(
    bet: int, prediction: int, token: str, db: Session
) -> RoundResult:
    repo = GameRepository.create(db)

    username = decode_access_token(access_token=token)["username"]

    try:
        game = get_game_object(username=username, repo=repo)

    except NoSuchGameException:
        raise NoSuchGameException

    round_result = game.compute_round_result(
        bet=bet, prediction=Prediction(int(prediction))
    )

    update_game(username=username, game=game, repo=repo)

    return round_result


def reset_game(token: str, db: Session) -> None:
    repo = GameRepository.create(db)
    username = decode_access_token(access_token=token)["username"]
    update_game(username=username, game=Game(name=username), repo=repo)


def update_game(username: str, game: Game, repo: GameRepository) -> None:
    repo.patch(
        target=GameState.username,
        search_term=username,
        patch_target="game",
        patch_value=game,
    )
