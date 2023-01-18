from sqlalchemy import Column, Integer, String

from api.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password_hash = Column(String, index=True)
    game = Column(String, index=True)
    round_info = Column(String, index=True)
    round_result = Column(String, index=True)
