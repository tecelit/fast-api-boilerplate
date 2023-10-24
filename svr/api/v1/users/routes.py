from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from core.dependencies import get_db
from fastapi.encoders import jsonable_encoder
from database.ops import users as user_ops
from database.models import User
from api.v1.users.schemas import *
from core.dependencies import *
from typing import List
from api.v1.users.auth import create_jwt_token, hash_password, verify_password

router = APIRouter()

@router.post("/register/", status_code=status.HTTP_201_CREATED)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        hashed_password = hash_password(user_data.password)
        db_user = user_ops.create_user(
            db,
            full_name=user_data.full_name,
            username=user_data.username,
            email=user_data.email,
            role=user_data.role,
            password_hash=hashed_password
        )
        # Generate JWT token for the registered user
        access_token = create_jwt_token(db_user)
        return jsonable_encoder({"access_token": access_token, "token_type": "bearer"})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/login/", response_model=UserLoginResponse, status_code=status.HTTP_200_OK)
def login_user(user_data: UserLogin, db: Session = Depends(get_db)):
    try:
        db_user = user_ops.get_user_by_email(db, user_data.email)
        if db_user is None or not verify_password(user_data.password, db_user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        access_token = create_jwt_token(db_user)
        user_login_response = UserLoginResponse(
            access_token=access_token,
            token_type="bearer",
            user_id=db_user.id,
            role=db_user.role
        )
        return jsonable_encoder(user_login_response)
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

# Logout Route
@router.post("/logout/", status_code=status.HTTP_200_OK)
def logout_user():
    return jsonable_encoder({})


@router.get("/protected")
def protected_route(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return jsonable_encoder(current_user)


@router.get("/protected_superadmin_only")
def protected_route(current_user: User = Depends(check_superadmin), db: Session = Depends(get_db)):
    return jsonable_encoder(current_user)


@router.get("/protected_admin_only")
def protected_route(current_user: User = Depends(check_admin), db: Session = Depends(get_db)):
    return jsonable_encoder(current_user)


@router.get("/protected_staff_only")
def protected_route(current_user: User = Depends(check_staff), db: Session = Depends(get_db)):
    return jsonable_encoder(current_user)




# @router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
# def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
#     try:
#         db_user = user_ops.create_user(
#             db,
#             full_name=user_data.full_name,
#             username=user_data.username,
#             email=user_data.email,
#             role=user_data.role
#         )
#         return jsonable_encoder(db_user)
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

# @router.get("/", response_model=List[UserResponse])
# def get_users(offset: int = Query(0, ge=0), limit: int = Query(10, ge=1), 
#             current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     try:
#         users = user_ops.get_users_with_pagination(db, offset=offset, limit=limit)
#         return users
    
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {str(e)}")
    

# @router.get("/{user_id}", response_model=UserResponse)
# def read_user(user_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     try:
#         if user_id != current_user.id:
#             raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You do not have access to this resource")

#         db_user = user_ops.get_user_by_id(db, user_id)
        
#         if db_user is None:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

#         return jsonable_encoder(db_user)
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {str(e)}")


# @router.put("/{user_id}", response_model=UserResponse)
# def update_user(user_id: int, user_data: UserBase, db: Session = Depends(get_db)):
#     try:
#         db_user = user_ops.get_user_by_id(db, user_id)
#         if db_user is None:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
#         db_user = user_ops.update_user(
#             db,
#             user=db_user,
#             full_name=user_data.full_name,
#             email=user_data.email,
#             role=user_data.role
#         )
#         return jsonable_encoder(db_user)
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# @router.delete("/{user_id}", response_model=dict)
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     try:
#         db_user = user_ops.get_user_by_id(db, user_id)
#         if db_user is None:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
#         user_ops.delete_user(db, db_user)
#         return {"message": "User deleted successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
