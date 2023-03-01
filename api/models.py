from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.database import Base


class UserDetail(Base):
    __tablename__ = "user_details"
    username = Column(String, primary_key=True, index=True)
    password_hash = Column(String, index=True)

    games = relationship("GameState", back_populates="user")

    def __repr__(self):
        return self.username


class GameState(Base):
    __tablename__ = "gamestates"
    id = Column(Integer, primary_key=True, index=True)
    game = Column(String, index=True)
    round_info = Column(String, index=True)
    round_result = Column(String, index=True)

    user = relationship("UserDetail", back_populates="games")
    username = Column(
        String, ForeignKey("user_details.username"), nullable=False
    )
