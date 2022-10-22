from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint

# USERS

class UserBase(BaseModel):
    pass

class UserEmail(UserBase):
    email: str

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        orm_mode = True

# POSTS

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    owner_id: int
    owner: UserEmail

    class Config:
        orm_mode = True

class PostResponseVotes(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True

# LOGIN

class UserLogin(UserBase):
    email: EmailStr
    password: str

# TOKEN

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

# VOTE

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1, ge=0)
