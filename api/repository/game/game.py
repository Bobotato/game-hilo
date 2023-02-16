from dataclasses import dataclass, field

from sqlalchemy import update
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from api.models import User
from api.repository.errors import GenericException


@dataclass
class GameRepository:
    __session: Session = field(default=None, repr=False)

    @classmethod
    def create(cls, session: Session) -> "GameRepository":
        return cls(session)

    def add(self, user: User):
        self.__session.add(user)
        self.__session.commit()

    def get(self, target: str, **filter):
        try:
            query = self.__session.query(target).filter_by(**filter).first()
            if query:
                return query

        except InvalidRequestError:
            raise InvalidRequestError("Filters are invalid.")

        raise GenericException

    def patch(self, target: str, search_term: str, **values) -> None:
        updater = update(User).where(target == search_term).values(**values)
        self.__session.execute(updater)
        self.__session.commit()
