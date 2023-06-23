from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from datetime import timedelta
from sqlalchemy.orm import Session

from schemas import schemas
from schemas.token import create_access_token
from schemas.hash import Hash
from schemas.oa2 import get_current_user
from models import models
from database import config



router = APIRouter(prefix="/login", tags=["Authentication"])


@router.post("/")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(config.get_db)):
    
    user: schemas.User = db.query(models.User).filter(
        models.User.username == request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    
    access_token = create_access_token(
        data={"sub": user.username}
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.get('/verify/', status_code=status.HTTP_200_OK)
def verify(current_user: schemas.User = Depends(get_current_user)):
    return {'status': 'success'}