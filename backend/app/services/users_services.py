from jwt import InvalidTokenError
from sqlalchemy.orm import Session
from models.user import *
from schemas.user import CreateUser, UpdateUser
from core.security import verify_password, password_hash
from core.config import SECRET_KEY, ALGORITHM
from datetime import datetime, timedelta
import jwt


def get_users(db: Session):
    return db.query(User).all()


def get_user_details(db: Session, username: str):
    user = db.query(User).filter(User.login == username).first()
    return user


def create_user(db: Session, user_data: CreateUser):
    if db.query(User).filter(User.login == user_data.login).first() is None:
        user = User(login=user_data.login, password=password_hash.hash(user_data.password))
        db.add(user)
        db.commit()
        db.refresh(user)
        return user.id
    else:
        return None


def update_user(db: Session, user_data: UpdateUser):
    user = db.query(User).filter(User.login == user_data.login).first()
    if user is None:
        return False
    else:
        user.password = password_hash.hash(user_data.password)
        db.commit()
        return True


def delete_user(db: Session, user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if user is not None:
        db.delete(user)
        db.commit()
        return True
    else:
        return False


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_details(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(db: Session, token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is not None:
            user = get_user_details(db, username)
            return user
        else:
            return None
    except InvalidTokenError:
        return None