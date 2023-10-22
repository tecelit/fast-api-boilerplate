from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.dependencies import get_db
from fastapi.encoders import jsonable_encoder
from database.ops import users as user_ops
from database.models import User
from api.v1.users.schemas import UserCreate, UserResponse, UserInDB, UserBase

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = user_ops.create_user(
            db,
            full_name=user_data.full_name,
            username=user_data.username,
            email=user_data.email,
            role=user_data.role
        )
        return jsonable_encoder(db_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    try:
        db_user = user_ops.get_user_by_id(db, user_id)
        if db_user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return jsonable_encoder(db_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserBase, db: Session = Depends(get_db)):
    try:
        db_user = user_ops.get_user_by_id(db, user_id)
        if db_user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        db_user = user_ops.update_user(
            db,
            user=db_user,
            full_name=user_data.full_name,
            email=user_data.email,
            role=user_data.role
        )
        return jsonable_encoder(db_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.delete("/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        db_user = user_ops.get_user_by_id(db, user_id)
        if db_user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        user_ops.delete_user(db, db_user)
        return {"message": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
