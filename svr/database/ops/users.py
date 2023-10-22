from sqlalchemy.orm import Session
from database.models import User

def create_user(db: Session, full_name: str, username: str, email: str, role: str):
    user = User(full_name=full_name, username=username, email=email, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

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
