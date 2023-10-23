from sqlalchemy.orm import Session
from database.models import User
from typing import List

def create_user(db: Session, full_name: str, username: str, email: str, role: str, password_hash: str):
    db_user = User(full_name=full_name, username=username, email=email, role=role, password_hash=password_hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users_with_pagination(db: Session, offset: int = 0, limit: int = 10) -> List[User]:
    users = db.query(User).offset(offset).limit(limit).all()
    return users

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user: User, full_name: str, email: str, role: str):
    user.full_name = full_name
    user.email = email
    user.role = role
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()
