from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..core.config import DATABASE_URL, connect_args
from contextlib import contextmanager


engine = create_engine(DATABASE_URL, echo=False, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()