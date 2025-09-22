from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.database import get_db
from db import models
from db.hash import Hash

router = APIRouter(
    tags=['authentication']
)

@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.DbUser).filter(models.DbUser.username == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Invalid credentials'
        )
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Incorrect password'
        )
    
    return {
        'access_token': user.username,
        'token_type': 'bearer',
        'user_id': user.id,
        'username': user.username
    }