from sqlalchemy.orm.session import Session
from db.models import DbArticle  
from schemas import ArticleBase
from fastapi import HTTPException, status

def create_article(db: Session, request: ArticleBase):
    new_article = DbArticle(
        title=request.title,
        content=request.content,
        user_id=request.creator_id,
        published=request.published
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def get_article(db: Session, id: int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first() 
    if not article:
        raise HTTPException(status_code=404, detail=f"Article with the id {id} is not available")
    return article