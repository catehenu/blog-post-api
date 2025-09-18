from pydantic import BaseModel
from typing import List, Optional

# User schemas
class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    items: List['ArticleDisplay'] = []

    class Config:
        orm_mode = True

# Article schemas
class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: UserDisplay

    class Config:
        orm_mode = True

# Update forward references
UserDisplay.update_forward_refs()
ArticleDisplay.update_forward_refs()