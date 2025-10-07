from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI(title="Social Media API")

class Post(BaseModel):
title: str
content: str
published: bool = True

    while True:
        try:
            conn = psycopg2.connect(host='localhost', database='fastapi', username='postgres', pasword='password123', cursor_factory=RealDictCursor)
            cursor = conn.cursor()
            print("Database connection was successful!")
            break
        except Exception as error:
            print("Connection to database failed!")
            print("Error:", error)
            time.sleep(2)

my_post_db = [
{
"id": 1,
"title": "my first post",
"content": "I love coding",
},
{
"id": 2,
"title": "fav food",
"content": "I love pizza",
}
]

def find_post(id):
for p in my_post_db:
if p["id"] == id:
return p

def find_index_post(id):
for i, p in enumerate(my_post_db):
if p["id"] == id:
return i

@app.get('/')
def root():
return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
cursor.execute("""SELECT \* FROM posts """)
posts = cursor.fetchall() # print(posts)
return {"data": posts}

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
post_dict = post.dict() #Convert pydantic model to dictionary
post_dict["id"] = randrange(0, 1000000) #Assign a random id to each post
my_post_db.append(post_dict)
print("New Post Added:", post_dict) # Debugging
print("Updated Database:", my_post_db) # Debugging
return {"data": "created post"}

@app.get("/posts/{id}")
def get_post(id: int):

    post = find_post(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    print(post)

    return {"post_detail": post}

@app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int): # logic for deleting post # find the index in the array that has the required ID # my_post.pop(index)
index = find_index_post(int(id))
if index == None:
raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post with id: {id} does not exist")
my_post_db.pop(index)
return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/post/{id}")
def update_post(id: int, post: Post):
index = find_index_post(int(id))
if index == None:
raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
detail="post with id: {id} does not exist")
post_dict = post.dict()
post_dict["id"] = id
my_post_db[index] = post_dict  
 return {"data": post_dict}
