from fastapi import APIRouter, HTTPException, Depends, status
from typing import List

from sqlalchemy.orm import Session
from db import get_db

from apps.auth.oauth2 import oauth2_schema, get_current_user

from . import schemas, db_queries

router = APIRouter(
    prefix='/item',
    tags=['item'],
)


@router.get('/get-all', response_model=List[schemas.ItemDetail])
# async def get_all(db: Session = Depends(get_db)):
async def get_all(db: Session = Depends(get_db), token: str = Depends(oauth2_schema)):
    return db_queries.get_all_item_posts(db)


@router.get('/{id}')
# @router.get('/{id}', response_model=schemas.ItemDetail)
# async def get_item(id: int = None, db: Session = Depends(get_db), token: str = Depends(oauth2_schema)):
async def get_item(id: int = None, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(get_current_user)):
    item = db_queries.get_item(db, id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There is no item post in db')
    # return item
    return {
        'data': item,
        'current_user': current_user
    }

@router.get('/')
# async def get_all(db: Session = Depends(get_db)):
async def get_item_by_title(title: str, db: Session = Depends(get_db), token: str = Depends(oauth2_schema)):
    item = db_queries.get_item_by_title(db, title)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There is no item post in db')
    return{
        'data' : item
    }


@router.post('/create', response_model=schemas.ItemCreate)
async def create_item(request: schemas.ItemCreate, db: Session = Depends(get_db)):
    return db_queries.create_item(db, request)


