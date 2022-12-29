from fastapi import APIRouter, HTTPException, status, Response, Depends
from sqlalchemy.orm import Session
from .. import schemes, database, models, oauth2

router = APIRouter(
    prefix="/vote",
    tags=['vote'])


@router.post("/", status_code=201)
def vote(vote: schemes.Vote, db: Session = Depends(database.get_db),
         current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="details not found")
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,
                                              models.Vote.user_id == current_user.id)

    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=409)
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"successful"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")

        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"deleted"}
