from fastapi import Request
from sqlalchemy.orm import Session
from database.db import SessionLocal
from fastapi import HTTPException, status, Depends
from core.config import settings
from api.v1.users.auth import get_current_user, oauth2_scheme

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


def get_current_user_dependency(token: str = Depends(oauth2_scheme)):
    return get_current_user(token)
