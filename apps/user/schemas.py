from pydantic import BaseModel
from typing import List

from apps.item.schemas import ItemShort
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class User(BaseModel):
    username: str
    email: str
    item_posts: List[ItemShort]

    class Config:
        from_attributes = True


class UserDetails(BaseModel):
    id: int
    username: str
    email: str
    item_posts: List[ItemShort]

    class Config:
        from_attributes = True


class UserShort(BaseModel):
    id: int
    username: str