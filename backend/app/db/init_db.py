from .base import Base
from .session import engine


def init_database():
    Base.metadata.create_all(bing=engine)
