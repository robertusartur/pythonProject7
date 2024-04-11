from sqlalchemy.orm.session import Session

from . import schemas, models


def get_all_item_posts(db: Session):
    return db.query(models.Item).all()


def get_item(db: Session, id: int = None):
    return db.query(models.Item).filter(models.Item.id == id).first()


def create_item(db: Session, request: schemas.ItemCreate):
    new_item = models.Item()
    new_item.published = request.published
    new_item.title = request.title
    new_item.description = request.description
    new_item.author_id = request.author_id

    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def get_item_by_title(db: Session, title: str):
    return db.query(models.Item).filter(models.Item.title == title).first()

