from jose import JWTError,jwt
from datetime import datetime,timedelta
from . import schemes,database,models
from  fastapi import Depends, status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings
oauth2_schema=OAuth2PasswordBearer(tokenUrl="login")
# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY=settings.screate_key
ALGORITHM=settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES=settings.access_token_expire_minutes
def create_access_token(data: dict):
     to_encode=data.copy()

     expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
     to_encode.update({"exp":expire})

     encodes=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
     return  encodes

def verify_token(token:str, creditials_exception):

    try:
     payload=jwt.decode(token, SECRET_KEY,[ALGORITHM])
     id:str=payload.get('user_id')
     if id is None:
          raise HTTPException(status_code=404, detail="gdvvf")

     token_data=schemes.TokenData(id=id)

    except JWTError:
         raise creditials_exception

    return token_data


def get_current_user(token:str=Depends(oauth2_schema),db:Session=Depends(database.get_db)):
    creditials_exception=HTTPException(status_code=403,detail="not ", headers={'WWW-Autheticate':"Bearer"})
    token= verify_token(token, creditials_exception)
    user= db.query(models.User).filter(models.User.id==token.id).first()
    return  user

