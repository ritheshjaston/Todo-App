from sqlalchemy import Column,Integer,String
from .database import Base


class Blog(Base):
    __tablename__='todolist'
    id=Column(Integer,primary_key=True,index=True)
    ItemName=Column(String)

