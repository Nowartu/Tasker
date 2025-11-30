from db.base import Base
from db.session import engine


def init_database():
    Base.metadata.create_all(bind=engine)
