from sqlalchemy.orm import Session

from app import models, schemas


def get_item(db: Session, item_id: int) -> models.Item | None:
    return db.get(models.Item, item_id)


def get_items(db: Session, skip: int = 0, limit: int = 100) -> list[models.Item]:
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.ItemCreate) -> models.Item:
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(
    db: Session, db_item: models.Item, item_update: schemas.ItemUpdate
) -> models.Item:
    update_data = item_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_item, field, value)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, db_item: models.Item) -> None:
    db.delete(db_item)
    db.commit()
