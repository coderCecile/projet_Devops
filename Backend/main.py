from typing import Union

from fastapi import FastAPI, Depends, HTTPException

from pydantic import BaseModel

from typing import List, Annotated
import models

from database import engine, SessionLocal
from sqlalchemy.orm import Session 


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    firstname:str
    last_name:str

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency= Annotated[Session, Depends(get_db)]

@app.post("/user")
async def create_user(user:UserBase, db:db_dependency):
    db_user= models.User(firstname=user.firstname, last_name= user.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}