from db.base import Base
from db.session import engine
from models.task import *
from models.comment import *


def init_database():
    Base.metadata.create_all(bind=engine)
