from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    full_name: str
    username: str
    email: EmailStr
    role: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "your_password"
            }
        }

class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str
    user_id: int
    role: str

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: int
    full_name: str
    username: str
    email: str
    role: str

    class Config:
        orm_mode = True

class UserInDB(UserBase):
    id: int

    class Config:
        orm_mode = True
