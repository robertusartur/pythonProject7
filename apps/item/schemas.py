from pydantic import BaseModel


class ItemCreate(BaseModel):
    title: str
    description: str
    published: bool
    author_id: int


class Item(ItemCreate):
    id: int

class ItemTitle(ItemCreate):
    title: str

class ItemShort(BaseModel):
    id: int
    title: str


class User(BaseModel):
    id: int
    username: str


class UserBase(BaseModel):
    id: int
    username: str
    email: str
    password: str


class ItemDetail(BaseModel):
    id: int
    title: str
    description: str
    published: bool
    author: User