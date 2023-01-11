from sqlalchemy import Column, Integer, String

from api.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password_hash = Column(String, index=True)
    access_token = Column(String, index=True)
