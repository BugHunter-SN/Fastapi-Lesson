from fastapi import FastAPI, Response, status, HTTPException, Depends
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import Optional, List


models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Social Media API")
    

@app.get('/')
def root():
    return {"message": "Social Media API"}
    

@app.get("/posts", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts      


@app.post('/posts', status_code=status.HTTP_201_CREATED, response_model=schemas.PostOut)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # print(**post.model_dump())
    new_post = models.Post(**post.model_dump())
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
   
    return new_post


@app.get("/posts/{id}", response_model=schemas.PostOut) 
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return post


@app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} does not exist")
    post.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/post/{id}", response_model=schemas.PostOut)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")
    
    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()
    return post_query.first()


@app.post('/users', status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user