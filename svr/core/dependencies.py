from fastapi import Request, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from database.db import SessionLocal
from jose import JWTError, jwt
from core.config import settings
from api.v1.users.auth import decode_jwt_token
from database.ops import users as user_ops
from database.models import User
from sqlalchemy.orm import Session

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

def get_current_user(token_data: dict = Depends(get_current_user_from_token), db: Session = Depends(get_db)) -> User:
    try:
        user_id = token_data.get("sub")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        
        db_user = user_ops.get_user_object(db, user_id)
        if db_user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        
        return db_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")


def check_superadmin(current_user: User = Depends(get_current_user)):
    """
    Dependency to check if the current user has the role "superadmin".
    """
    if current_user['role'] != "superadmin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission denied. Only superadmins can perform this action.")
    return current_user


def check_admin(current_user: User = Depends(get_current_user)):
    """
    Dependency to check if the current user has the role "admin".
    """
    if current_user['role'] not in ["superadmin", "admin"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission denied. Only admins can perform this action.")
    return current_user


def check_staff(current_user: User = Depends(get_current_user)):
    """
    Dependency to check if the current user has the role "staff".
    """
    if current_user['role'] not in ["superadmin", "admin", "staff"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission denied. Only staff can perform this action.")
    return current_user
