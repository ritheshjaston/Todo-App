from fastapi import FastAPI,Depends
from . import schemas,models
from .database import engine,get_db
from sqlalchemy.orm import Session
import uvicorn

app=FastAPI()


models.Base.metadata.create_all(engine)

@app.post('/todolstAdd')
def create(req:schemas.Blog,db:Session=Depends(get_db)):
    new=models.Blog(ItemName=req.ItemName)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@app.get("/getList")
def getblogs(db:Session=Depends(get_db)):
    blog=db.query(models.Blog).all()
    return blog

@app.delete("/deleteList")
def delete(id,db:Session=Depends(get_db)):
    entity=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not entity:
        return "Not Exist"
    db.delete(entity)
    db.commit()
    return "Successfully Deleted"

@app.put('/todolstupdate')
def create(req:schemas.updatetodo,db:Session=Depends(get_db)):
    todo_item = db.query(models.Blog).filter(models.Blog.id == req.Id).first()
    if not todo_item:
        return "Not Found"
    
    todo_item.ItemName=req.ItemName
    db.commit()
    db.refresh(todo_item)
    return todo_item


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0")