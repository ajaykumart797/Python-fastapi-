from  .. import schemes,models,utils
from .. database import get_db
from fastapi import Depends,HTTPException,status,Response,APIRouter
from sqlalchemy.orm import Session

router=APIRouter(prefix="/users",
                 tags=['users'])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemes.UserOut)
def create_user(user: schemes.UserCreate, db: Session = Depends(get_db)):
    Hashed_opassword= utils.hash(user.password)
    user.password =Hashed_opassword
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemes.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user_details = db.query(models.User).filter(models.User.id == id).first()
    if user_details == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return user_details
