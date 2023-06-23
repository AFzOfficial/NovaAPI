from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from schemas import schemas
from models import models
from database import config
from api import user


router = APIRouter(tags=["Users"], prefix="/users")
get_db = config.get_db



# Create User
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


# Get Users
@router.get("/", status_code=status.HTTP_200_OK, response_model=list[schemas.ShowUser])
def get_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return user.get_all(db)


# Get Users using the ID
# @router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
# def get_user_by_id(id: int, db: Session = Depends(get_db)):
#     return user.get(id, db)


# Get Users using the USERNAME
@router.get("/{username}", status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    return user.get_by_username(username, db)