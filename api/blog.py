from sqlalchemy.orm import Session
from schemas import schemas
from models import models
from fastapi import HTTPException, status


# Get All Posts
def get_all(db: Session, skip: int = 0, limit: int = 100):
    posts = db.query(models.Post).offset(skip).limit(limit).all()
    return posts


# Create Post
def create(request: schemas.PostBase, db: Session):
    new_post = models.Post(title=request.title, content=request.content, user_id=1)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# Delete Post
def delete(id: int, db: Session):
    post = db.query(models.Post).filter(models.Post.id == id)

    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")
    
    post.delete(synchronize_session=False)
    db.commit()
    return {'status':'success'}


# Update Post
def update(id: int, request: schemas.Post, db: Session):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")
    post.update(request.__dict__)
    db.commit()
    return {'status':'success'}


# Get One Post
def get(id: int, db: Session):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if post:
        return post
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with the id {id} is not found")