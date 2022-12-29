# from fastapi import APIRouter,HTTPException,status,Response,Depends
# from  sqlalchemy.orm import Session
#
# from .. import database,models,schemes,utils
#
# router=APIRouter(tags=["attr"])
#
# @router.post('/login')
# def login(user_creditials:schemes.Userlogin, db:Session=Depends(database.get_db)):
#     user=db.query(models.User ).filter(models.User.email==user_creditials.email).first()
#     if not user:
#         raise HTTPException(status_code=404,detail="bjjgffd")
#
#     if not utils.verify(user.password, user_creditials.password):
#         raise  HTTPException(status_code=404,detail="unn")
#
#         return {"token"}

#
from fastapi  import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import  database, schemes,models,utils,oauth2

router=APIRouter(tags=["Authetication"])

@router.post("/login",response_model=schemes.Token)
def login(user_creditials:OAuth2PasswordRequestForm=Depends(), db:Session =Depends(database.get_db) ):
    user= db.query(models.User).filter(models.User.email==user_creditials.username).first()
    if not  user:
        raise HTTPException(status_code=403,detail="invalid cred")

    if not utils.verify(user_creditials.password, user.password):
        raise HTTPException(status_code=403, detail="invalid cred")


    access_token=oauth2.create_access_token(data={"user_id":user.id})
    return {"access_token":access_token,"token_type":"bearer_token"}

