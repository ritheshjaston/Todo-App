from pydantic import BaseModel

class Blog(BaseModel):
    ItemName:str

class updatetodo(BaseModel):
    Id:int
    ItemName:str