from db.base import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(50), unique=True, nullable=False)
    password = Column(String(128), nullable=True)
