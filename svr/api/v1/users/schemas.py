from pydantic import BaseModel

class UserBase(BaseModel):
    full_name: str
    username: str
    email: str
    role: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

class UserInDB(UserBase):
    id: int

    class Config:
        orm_mode = True
