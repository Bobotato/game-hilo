from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.database import Base


class UserDetail(Base):
    __tablename__ = "user_details"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password_hash = Column(String, index=True)

    game_states = relationship("GameState", back_populates="user_details")


class GameState(Base):
    __tablename__ = "gamestates"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user_details.id"))
    game = Column(String, index=True)
    round_info = Column(String, index=True)
    round_result = Column(String, index=True)

    user_details = relationship("UserDetail", back_populates="game_states")
