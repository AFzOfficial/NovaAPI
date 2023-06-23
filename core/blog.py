from schemas.oa2 import get_current_user
from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from api import blog
from schemas import schemas
from database import config


router = APIRouter(tags=["Posts"], prefix="/posts")
get_db = config.get_db


# Get All Posts
@router.get("/", response_model=list[schemas.ShowPost])
def get_all_posts(db: Session = Depends(get_db), skip: int = 0, limit: int = 100): #  , current_user: schemas.User = Depends(get_current_user)
    return blog.get_all(db)

# Create Post
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_post(request: schemas.Post, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create(request, db)

# Get One Post using the ID
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowPost)
def get_post_by_id(id: int, response: Response, db: Session = Depends(get_db)): # , current_user: schemas.User = Depends(get_current_user)
    return blog.get(id, db)

# Delete Post
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.delete(id, db)

# Update Post
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_post(id: int, request: schemas.Post, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.update(id, request, db)