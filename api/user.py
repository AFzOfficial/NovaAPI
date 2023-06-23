from sqlalchemy.orm import Session
from schemas import schemas
from models import models
from fastapi import HTTPException, status
from schemas.hash import Hash


# Create User
def create(request: schemas.User, db: Session):
    hashedPassword = Hash.bcrypt(request.password)
    user = models.User(username=request.username, password=hashedPassword)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# Get One User using the ID
def get(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    return user


# Get One User using the USERNAME
def get_by_username(username: str, db: Session):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"User with username {username} not found")
    return user



# Get All Users
def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()