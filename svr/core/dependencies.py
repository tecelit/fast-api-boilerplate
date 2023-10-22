from fastapi import Request
from sqlalchemy.orm import Session
from database.db import SessionLocal

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
