from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from core.config import settings
from database.models import User
import bcrypt
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

ALGORITHM = settings.ALGORITHM
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_jwt_token(user: User) -> str:
    token_data = {
        "sub": user.id,
        "role": user.role
    }
    return jwt.encode(token_data, settings.SECRET_KEY, algorithm=ALGORITHM)

def decode_jwt_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    payload = decode_jwt_token(token)
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user_id
