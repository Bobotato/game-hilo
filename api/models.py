from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password_hash = Column(String, index=True)
    game_info = relationship("GameInfo", back_populates="user")


class GameInfo(Base):
    __tablename__ = "gameinfo"
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="game_info")

    id = Column(Integer, primary_key=True, index=True)
    game_state = Column(String, index=True)
    player = Column(String, index=True)
    current_card = Column(String, index=True)
    drawn_card = Column(String, index=True)
    win = Column(Boolean, index=True)
    is_player_bankrupt = Column(Boolean, index=True)
    is_deck_empty = Column(Boolean, index=True)
