import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.main import app
from db.base import Base
from services.users_services import create_user
from schemas.user import CreateUser

from backend.app.db.session import get_db
from backend.app.services import utils

# test database in RAM
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_database.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """
    Creates new database for each test
    """
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    create_user(db, CreateUser(login="admin", password="admin"))
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    """
    TestClient FastAPI with overwrote database.
    """

    def override_get_db():
        yield db_session


    async def override_get_current_user():
        return {"test": "test"}


    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[utils.get_current_user] = override_get_current_user

    with TestClient(app) as c:
        yield c