# schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


# Token
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


# User schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    created_at: datetime

    class Config:
        orm_mode = True


# Post schemas
class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    is_approved: Optional[bool] = None


class PostDelete(BaseModel):
    success: bool
    message: str


class PasswordChange(BaseModel):
    current_password: str
    new_password: str


class PasswordChangeResponse(BaseModel):
    message: str


class Post(PostBase):
    id: int
    is_approved: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    user_id: int
    user: User

    class Config:
        orm_mode = True