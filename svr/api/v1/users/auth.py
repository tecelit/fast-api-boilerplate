from jose import JWTError, jwt
from fastapi import HTTPException, status
from core.config import settings
from database.models import User
from fastapi.security import HTTPBearer
from passlib.context import CryptContext
from datetime import timedelta, datetime
from passlib.exc import PasslibSecurityError

ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

bearer_scheme = HTTPBearer()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    try:
        return pwd_context.hash(password)
    
    except PasslibSecurityError as e:
        print(f"Error hashing password: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Could not hash password")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return pwd_context.verify(plain_password, hashed_password)
    
    except PasslibSecurityError as e:
        print(f"Error verifying password: {e}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")


def create_jwt_token(user: User) -> str:
    try:
        expiration_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        token_data = {
            "sub": str(user.id), 
            "role": user.role,
            "exp": expiration_time
        }
    
        token = jwt.encode(token_data, settings.SECRET_KEY, algorithm=ALGORITHM)
        return token
    
    except JWTError as e:
        print(f"Error encoding token: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Could not create token")


def decode_jwt_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    
    except JWTError as e:
        print(f"Error decoding token: {e}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
