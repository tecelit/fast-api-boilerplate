from sqlalchemy.orm import Session
from database.models import User
from typing import List, Optional
from sqlalchemy.exc import SQLAlchemyError

def create_user(db: Session, full_name: str, username: str, email: str, role: str, password_hash: str):
    try:
        db_user = User(full_name=full_name, username=username, email=email, role=role, password_hash=password_hash)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def get_users_with_pagination(db: Session, offset: int = 0, limit: int = 10) -> List[User]:
    try:
        users = db.query(User).offset(offset).limit(limit).all()
        return users
    except SQLAlchemyError as e:
        raise e

def get_user_by_username(db: Session, username: str):
    try:
        return db.query(User).filter(User.username == username).first()
    except SQLAlchemyError as e:
        raise e

def get_user_by_email(db: Session, email: str):
    try:
        return db.query(User).filter(User.email == email).first()
    except SQLAlchemyError as e:
        raise e

def get_user_by_id(db: Session, user_id: int):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        return user
    except SQLAlchemyError as e:
        raise e
    
def get_user_object(db: Session, user_id: int) -> Optional[dict]:
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user_data = {
                "id": user.id,
                "full_name": user.full_name,
                "username": user.username,
                "email": user.email,
                "role": user.role
            }
            return user_data
        else:
            return None
    except Exception as e:
        raise e

def update_user(db: Session, user: User, full_name: str, email: str, role: str):
    try:
        user.full_name = full_name
        user.email = email
        user.role = role
        db.commit()
        db.refresh(user)
        return user
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def delete_user(db: Session, user: User):
    try:
        db.delete(user)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e
