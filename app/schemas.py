from pydantic import BaseModel
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
        from_attributes=True