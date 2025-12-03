from fastapi import Depends, HTTPException
from db.session import get_db
from core.security import oauth2_scheme
from services import users_services


def get_current_user(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = users_services.get_current_user(db, token)
    if user is not None:
        return user
    else:
        raise credentials_exception