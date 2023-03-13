from dataclasses import dataclass, field

from sqlalchemy import update
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from api.models import GameState
from api.repository.errors import NoSuchGameException
from api.repository.pickler import unpickle_object
from hilo.game import Game


@dataclass
class GameRepository:
    __session: Session = field(default=None, repr=False)

    @classmethod
    def create(cls, session: Session) -> "GameRepository":
        return cls(session)

    def add(self, user: GameState) -> None:
        self.__session.add(user)
        self.__session.commit()

    def get(self, target: str, **filter) -> Game:
        try:
            query = self.__session.query(target).filter_by(**filter).first()

            if query:
                return unpickle_object(query["game"])

            raise NoSuchGameException

        except InvalidRequestError:
            raise InvalidRequestError("Filters are invalid.")

    def patch(self, target: str, search_term: str, **values) -> None:
        updater = (
            update(GameState).where(target == search_term).values(**values)
        )
        self.__session.execute(updater)
        self.__session.commit()
