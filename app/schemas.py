from pydantic import BaseModel, EmailStr
from datetime import datetime

    
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class PostCreate(PostBase):
    pass

# class PostUpdate(PostBase):
#     title: str
#     content: str
#     published: bool


    
class PostOut(PostBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
        
        
        
class UserBase(BaseModel):
    email: EmailStr
    password: str
    created_at: datetime
    
class UserCreate(UserBase):
    pass


class UserOut(UserBase):
    id: int
    email: EmailStr
    created_at: datetime