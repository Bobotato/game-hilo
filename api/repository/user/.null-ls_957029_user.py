from dataclasses import dataclass, field

from sqlalchemy import column, text
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from api.models import User
from api.repository.errors import GenericException


@dataclass
class UserRepository:
    __session: Session = field(default=None, repr=False)

    @classmethod
    def create(cls, session: Session) -> "UserRepository":
        return cls(session)

    def add(self, user: User):
        self.__session.add(user)
        self.__session.commit()
        self.__session.refresh(user)

    def get(self, target: str, **filter):
        try:
            query = (
                self.__session.query(column(target))
                .filter_by(**filter)
                .first()
            )
            if query:
                return query

        except InvalidRequestError:
            raise InvalidRequestError("Filters are invalid.")

        raise GenericException

    def test(self):
        return type(self.__session.query(User.password_hash).first())
