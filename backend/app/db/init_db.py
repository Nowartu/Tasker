from db.base import Base
from db.session import engine, SessionLocal
from models.task import *
from models.comment import *
from models.user import *
from schemas.user import CreateUser
from services.users_services import create_user


async def init_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    create_user(db, CreateUser(login="admin", password="admin"))