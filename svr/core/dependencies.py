from fastapi import Request, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from database.db import SessionLocal
from jose import JWTError, jwt
from core.config import settings
from api.v1.users.auth import decode_jwt_token
from database.ops import users as user_ops

bearer_scheme = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def setup_db_dependency(app):
    """
    Dependency setup function to add the database session dependency to the app.
    """
    app.dependency_overrides[get_db] = get_db

def get_current_user_from_token(token: str = Depends(bearer_scheme)) -> dict:
    try:
        payload = decode_jwt_token(token.credentials)
        return payload
    except JWTError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

def get_current_user(token_data: dict = Depends(get_current_user_from_token)) -> dict:
    try:
        user_id = token_data.get("sub")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        
        return user_id
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
