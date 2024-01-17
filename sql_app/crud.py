from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_sheets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Sheet).offset(skip).limit(limit).all()


def create_user_sheet(db: Session, sheet: schemas.SheetCreate, user_id: int):
    db_sheet = models.Sheet(**sheet.dict(), owner_id=user_id)
    db.add(db_sheet)
    db.commit()
    db.refresh(db_sheet)
    return db_sheet
